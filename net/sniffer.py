import socket

class Sniffer(object):
    def __init__(self, queue):
        self.queue = queue
        self.HOST = socket.gethostbyname(socket.gethostname())
        self.s = None
        self.b_size = 65565
        self.ativo = True

    def start_listening(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        self.s.bind((self.HOST, 0))
        self.s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        self.s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        while self.ativo:
            self.queue.put(self.s.recv(self.b_size))



    def stop(self):
        print('Finalizando Servidor...')
        self.iniciado = True
        self.ativo = False
        self.s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        exit(0)
