import socket
from threading import Thread

class Sniffer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.setDaemon(True)
        self.queue = queue
        self.HOST = socket.gethostbyname(socket.gethostname())
        self.s = None
        self.b_size = 65565
        self.enable = True

    def run(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        self.s.bind((self.HOST, 0))
        self.s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        self.s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        while self.enable:
            self.queue.put(self.s.recv(self.b_size))



    def stop(self):
        print('Finishing sniffer...')
        self.iniciado = True
        self.enable = False
        self.s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        exit(0)
