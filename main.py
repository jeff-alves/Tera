import argparse

from core.block_splitter import BlockSplitter
from core.connection_handler import ConnectionHandler
from core.messages_handler import MessagesHandler
from net.sniffer import Sniffer


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tera sniffer')
    parser.add_argument('-n', default='0')
    args = parser.parse_args()

    try:
        msg_handler = MessagesHandler()
        c_splitter = BlockSplitter(1, msg_handler.messages)
        s_splitter = BlockSplitter(2, msg_handler.messages)
        con_handler = ConnectionHandler(c_splitter, s_splitter)
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

        con_handler.join(1000)
        s_splitter.join(1000)
        c_splitter.join(1000)
        msg_handler.join(1000)
        print('Saindo')
        exit(0)
