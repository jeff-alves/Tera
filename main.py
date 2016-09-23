import os
import sys

import argparse

from core.block_splitter import BlockSplitter
from core.connection_handler import ConnectionHandler
from core.messages_handler import MessagesHandler
from net.sniffer import Sniffer
import win32com.shell.ShellExecuteEx


def elevate():
    import ctypes, win32event, win32process
    outpath = r'%s\%s.out' % (os.environ["TEMP"], os.path.basename(__file__))
    if ctypes.windll.shell32.IsUserAnAdmin():
        if os.path.isfile(outpath):
            sys.stderr = sys.stdout = open(outpath, 'w', 0)
        return
    with open(outpath, 'w+', 0) as outfile:
        hProc = win32com.shell.ShellExecuteEx(lpFile=sys.executable, \
            lpVerb='runas', lpParameters=' '.join(sys.argv), fMask=64, nShow=0)['hProcess']
        while True:
            hr = win32event.WaitForSingleObject(hProc, 40)
            while True:
                line = outfile.readline()
                if not line: break
                sys.stdout.write(line)
            if hr != 0x102: break
    os.remove(outpath)
    sys.stderr = ''
    sys.exit(win32process.GetExitCodeProcess(hProc))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tera sniffer')
    parser.add_argument('-n', default='0')
    args = parser.parse_args()

    try:
        msg_handler = MessagesHandler()
        c_splitter = BlockSplitter(1, msg_handler.messages)
        s_splitter = BlockSplitter(2, msg_handler.messages)
        con_handler = ConnectionHandler(msg_handler, c_splitter, s_splitter)
        sniffer = Sniffer(con_handler.queue)

        msg_handler.start()
        c_splitter.start()
        s_splitter.start()
        con_handler.start()
        sniffer.start_listening()

    except KeyboardInterrupt:
        print('Ctrl+C')
        sniffer.stop()
        con_handler.stop()
        s_splitter.stop()
        c_splitter.stop()
        msg_handler.stop()

        con_handler.join(100)
        s_splitter.join(100)
        c_splitter.join(100)
        msg_handler.join(100)
        print('Saindo')
        exit(0)
