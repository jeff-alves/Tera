from Queue import Queue
from threading import Thread
from game.C_CHECK_VERSION import C_CHECK_VERSION

class MessagesHandler(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.messages = Queue()
        self.opcodes = None
        self.ativo = True
        self.C_CHECK_VERSION = None

    def run(self):
        while not self.C_CHECK_VERSION:
            msg = self.messages.get()
            if msg[2] == 19900:
                self.C_CHECK_VERSION = C_CHECK_VERSION(msg)
                print('Using opcodes v: ' + str(self.C_CHECK_VERSION.ver[0][1]))
                self.opcodes = {}
                with open('opcodes/' + str(self.C_CHECK_VERSION.ver[0][1]) + '.txt') as f:
                    for line in f:
                        (val, key) = line.split(" = ")
                        self.opcodes[int(key)] = val
        while self.ativo:
            msg = self.messages.get()
            try:
                # eval(self.opcodes[msg[2]])(msg[0], msg[1], msg[3])
                print(self.opcodes[msg[2]], msg[3].get_array_int(1))
            except Exception as e:
                print(e)
                print(msg[1], msg[2], msg[3].get_array_int(1))

    def stop(self):
        self.ativo = False
