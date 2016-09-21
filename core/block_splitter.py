from Queue import Queue
from datetime import datetime
from threading import Thread
from core.bytes import Bytes

class BlockSplitter(Thread):

    def __init__(self, direction, msg_queue):
        Thread.__init__(self)
        self.setDaemon(True)
        self.bytes = Queue()
        self.enable = True
        self.msg_queue = msg_queue
        self.direction = direction

    def run(self):
        while self.enable:
            block_size = self.bytes.get() | self.bytes.get() << 8
            opcode = self.bytes.get() | self.bytes.get() << 8
            block = Bytes()
            while block.len() < block_size - 4:
                block.append(self.bytes.get())
            self.msg_queue.put((datetime.utcnow(), self.direction, opcode, block))

    def stop(self):
        self.enable = False

    def add_data(self, data):
        for byte in data:
            self.bytes.put(byte)
