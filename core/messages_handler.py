# from ConfigParser import ConfigParser
from Queue import Queue
from threading import Thread

from game.message.C.C_CHECK_VERSION import C_CHECK_VERSION

class MessagesHandler(Thread):

    def __init__(self, tracker, servers_db, opcodes_db):
        Thread.__init__(self)
        self.setDaemon(True)
        self.messages = Queue()
        self.enable = True
        self.opcodes_db = opcodes_db
        self.servers_db = servers_db
        self.tracker = tracker

    def run(self):
        while not self.opcodes_db.opcodes_v:
            msg = self.messages.get()
            if msg[2] == 19900:
                self.opcodes_db.read(str(C_CHECK_VERSION(self.tracker, msg[0], msg[1], msg[2], msg[3], None).ver[0][1]))

        print('Using opcodes: ' + str(self.opcodes_db.opcodes_v))
        while self.enable:
            msg = self.messages.get()
            cls = self.opcodes_db.get(msg[2])
            if cls:
                try:
                    cls(self.tracker, msg[0], msg[1], msg[2], msg[3], self.servers_db.selected[1])
                except Exception as e:
                    print(e, cls, msg[3].get_array_hex(1))

    def stop(self):
        self.enable = False
