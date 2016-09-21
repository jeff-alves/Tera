from Queue import Queue
from threading import Thread

from crypt.session import Session
from net.ip import Ip
from net.tcp import Tcp


class ConnectionHandler(Thread):

    def __init__(self, c_splitter, s_splitter):
        Thread.__init__(self)
        self.setDaemon(True)
        self.server_ip = None
        self.queue = Queue()
        self.ativo = True
        self.server_keys = []
        self.client_keys = []
        self.c_splitter = c_splitter
        self.s_splitter = s_splitter

    def run(self):
        print('Waiting to server connection start...')
        while not self.server_ip:
            ip = Ip(self.queue.get())
            if ip.protocol != 6: continue
            tcp = Tcp(ip.data)
            if len(tcp.data) == 4  and tcp.data.get_array_int(1) == [1, 0, 0, 0]:
                self.server_ip = ip.source_addr
                print('Server ip: ' + self.server_ip)

        while len(self.server_keys) < 2 or len(self.client_keys) < 2:
            ip = Ip(self.queue.get())
            if ip.protocol != 6 or (ip.source_addr != self.server_ip and ip.destination_addr != self.server_ip): continue
            tcp = Tcp(ip.data)
            if tcp.data.len() == 128:
                if ip.source_addr == self.server_ip:  # recebido
                    self.server_keys.append(tcp.data)
                else:  # enviado
                    self.client_keys.append(tcp.data)

        self.session = Session(self.server_keys, self.client_keys)

        while self.ativo:
            ip = Ip(self.queue.get())
            if ip.protocol != 6 or (ip.source_addr != self.server_ip and ip.destination_addr != self.server_ip): continue
            tcp = Tcp(ip.data)
            if not tcp.data.len(): continue
            if ip.source_addr == self.server_ip:  # recebido
                self.session.encrypt(tcp.data)
                self.s_splitter.add_data(tcp.data)
            else:  # enviado
                self.session.decrypt(tcp.data)
                self.c_splitter.add_data(tcp.data)

    def stop(self):
        self.ativo = False

