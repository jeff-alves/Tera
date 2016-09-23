from Queue import Queue
from threading import Thread

from game.message.client.C_CHECK_VERSION import C_CHECK_VERSION
from game.message.parse_opcodes import parse_opcodes
from game.trackers.player import Player


class MessagesHandler(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.messages = Queue()
        self.opcodes = None
        self.enable = True
        self.C_CHECK_VERSION = None
        self.region = None
        self.player = Player()

    def run(self):
        while not self.C_CHECK_VERSION:
            msg = self.messages.get()
            if msg[2] == 19900:
                self.C_CHECK_VERSION = C_CHECK_VERSION(msg[0], msg[1], msg[2], msg[3], self.region)
                opcodes_v = str(self.C_CHECK_VERSION.ver[0][1])
                print('Using opcodes ver: ' + opcodes_v)
                self.opcodes = parse_opcodes(opcodes_v)

        while self.enable:
            msg = self.messages.get()
            cls = self.opcodes.get(msg[2])
            if cls:
                try:
                    cls(msg[0], msg[1], msg[2], msg[3], self.region)  # create game opcode class
                    print(cls)
                except Exception as e:
                    print(e, self.opcodes[msg[2]], msg[3].get_array_int(1))

    def stop(self):
        self.enable = False
