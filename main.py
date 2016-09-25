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
        con_handler = ConnectionHandler(msg_handler, c_splitter, s_splitter)
        sniffer = Sniffer(con_handler.queue)

        msg_handler.start()
        c_splitter.start()
        s_splitter.start()
        con_handler.start()
        sniffer.start()

        msg_handler.join()

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
