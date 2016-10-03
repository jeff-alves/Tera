from core.block_splitter import BlockSplitter
from core.connection_handler import ConnectionHandler
from core.messages_handler import MessagesHandler
from game.message.opcodes_database import OpcodesDatabase
from game.services.abnormal_database import AbnormalDatabase
from game.services.hot_dot_database import HotDotDatabase
from game.services.icon_database import IconDatabase
from game.services.npc_database import NpcDatabase
from game.services.server_database import ServerDatabase
from game.services.skill_database import SkillDatabase
from game.tracker import Tracker
from net.sniffer import Sniffer
from util.enums import MessageDirection


if __name__ == '__main__':
    try:
        print('Reading databases...')
        servers_db = ServerDatabase()
        abnormal_db = AbnormalDatabase()
        hot_dot_db = HotDotDatabase()
        icon_db = IconDatabase()
        npc_db = NpcDatabase()
        skill_db = SkillDatabase()
        opcodes_db = OpcodesDatabase()
        tracker = Tracker()

        msg_handler = MessagesHandler()
        c_splitter = BlockSplitter(MessageDirection(1), msg_handler.messages)
        s_splitter = BlockSplitter(MessageDirection(2), msg_handler.messages)
        con_handler = ConnectionHandler(c_splitter, s_splitter)
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
        print('Exiting')
        exit(0)
