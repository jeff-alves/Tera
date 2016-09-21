from _struct import unpack
from core.bytes import Bytes

class Tcp(object):
    def __init__(self, data):
        tcp_header = data[0:20]
        tcph = unpack('!HHLLHHHH', tcp_header)
        # self.source_port = tcph[0]
        # self.destination_port = tcph[1]
        # self.sequence_number = tcph[2]
        # self.ack_number = tcph[3]
        self.offset = tcph[4] >> 12
        header_length = self.offset * 4
        # self.reserved = (tcph[4] >> 9) & 0b111
        # self.ns = (tcph[4] >> 8) & 0b1
        # self.cwr = (tcph[4] >> 7) & 0b1
        # self.ece = (tcph[4] >> 6) & 0b1
        # self.urg = (tcph[4] >> 5) & 0b1
        # self.ack = (tcph[4] >> 4) & 0b1
        # self.psh = (tcph[4] >> 3) & 0b1
        # self.rst = (tcph[4] >> 2) & 0b1
        # self.syn = (tcph[4] >> 1) & 0b1
        # self.fin = tcph[4] & 0b1
        # self.window_size = tcph[5]
        # self.checksum = tcph[6]
        # self.urg_pointer = tcph[7]
        # self.options = None
        self.data = Bytes(data[header_length:])

        # opt_lenght = header_length - 20
        # if opt_lenght:
            # self.options = unpack('!' + (opt_lenght * 'B'), data[20:header_length])

    # def __str__(self):
        # return ', \t'.join((str(self.source_port), str(self.destination_port), str(self.sequence_number), str(self.ack_number), str(self.offset), str(self.reserved), str(self.ns), str(self.cwr), str(self.ece), str(self.urg), str(self.ack), str(self.psh), str(self.rst), str(self.syn), str(self.fin), str(self.window_size), str(self.checksum), str(self.urg_pointer), str(self.options)))
