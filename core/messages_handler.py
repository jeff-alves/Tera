# from ConfigParser import ConfigParser
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
        self.opcodes_v = None
        self.region = None
        self.player = Player()

    def run(self):
        while not self.opcodes_v:
            msg = self.messages.get()
            if msg[2] == 19900:
                self.opcodes_v = str(C_CHECK_VERSION(msg[0], msg[1], msg[2], msg[3], self.region).ver[0][1])
        self.opcodes = parse_opcodes(self.opcodes_v)
        print('Using opcodes: ' + str(self.opcodes_v))
        while self.enable:
            msg = self.messages.get()
            cls = self.opcodes.get(msg[2])
            if cls:
                try:
                    cls(msg[0], msg[1], msg[2], msg[3], self.region)  # create game opcode class
                except Exception as e:
                    print(e, self.opcodes[msg[2]], msg[3])

    def stop(self):
        self.enable = False
