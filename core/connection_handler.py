from Queue import Queue
from threading import Thread
from mock import self
from crypt.session import Session
from net.ip import Ip
from net.tcp import Tcp

class ConnectionHandler(Thread):

    def __init__(self, servers_db, c_splitter, s_splitter):
        Thread.__init__(self)
        self.setDaemon(True)
        self.queue = Queue()
        self.enable = True
        self.c_splitter = c_splitter
        self.s_splitter = s_splitter
        self.server_keys = []
        self.client_keys = []
        self.servers_db = servers_db

    def run(self):
        print('Waiting to initial connection to server...')
        while not self.servers_db.selected:
            ip = Ip(self.queue.get())
            if ip.protocol != 6: continue
            tcp = Tcp(ip.data)
            if len(tcp.data) == 4  and tcp.data.get_array_int(1) == [1, 0, 0, 0]:
                self.servers_db.selected = self.servers_db[ip.source_addr]
        print('Conected to: ' + self.servers_db.selected[3])
        while len(self.server_keys) < 2 or len(self.client_keys) < 2:
            ip = Ip(self.queue.get())
            if ip.protocol != 6 or (ip.source_addr != self.servers_db.selected[0] and ip.destination_addr != self.servers_db.selected[0]): continue
            tcp = Tcp(ip.data)
            if tcp.data.len() == 128:
                if ip.source_addr == self.servers_db.selected[0]:  # received
                    self.server_keys.append(tcp.data)
                else:  # sent
                    self.client_keys.append(tcp.data)
        self.session = Session(self.server_keys, self.client_keys)
        while self.enable:
            ip = Ip(self.queue.get())
            if ip.protocol != 6 or (ip.source_addr != self.servers_db.selected[0] and ip.destination_addr != self.servers_db.selected[0]): continue
            tcp = Tcp(ip.data)
            if not tcp.data.len(): continue
            if ip.source_addr == self.servers_db.selected[0]:  # received
                self.session.encrypt(tcp.data)
                self.s_splitter.add_data(tcp.data)
            else:  # sent
                self.session.decrypt(tcp.data)
                self.c_splitter.add_data(tcp.data)

    def stop(self):
        self.enable = False

