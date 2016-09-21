from _struct import unpack
import socket

class Ip(object):
    def __init__(self, data):
        ip_header = data[0:20]
        iph = unpack('!BBHHHBBH4s4s', ip_header)
        # self.version = iph[0] >> 4
        self.ihl = iph[0] & 0b1111
        header_length = self.ihl * 4
        # self.dscp = iph[1] >> 2
        # self.ecn = iph[1] & 0b11
        # self.total_length = iph[2]
        # self.identification = iph[3]
        # self.evil_bit = (iph[4] >> 15) & 0b1
        # self.df = (iph[4] >> 14) & 0b1
        # self.mf = (iph[4] >> 13) & 0b1
        # self.fragment_offset = iph[4] & 0b1111111111111
        # self.ttl = iph[5]
        self.protocol = iph[6]
        # self.checksum = iph[7]
        self.source_addr = socket.inet_ntoa(iph[8]);
        self.destination_addr = socket.inet_ntoa(iph[9]);
        # self.options = None
        self.data = data[header_length:]

        # opt_lenght = header_length - 20
        # if opt_lenght:
        #    self.options = unpack('!' + (opt_lenght * 'B'), data[20:header_length])


    # def __str__(self):
        # return ', \t'.join((str(self.version), str(self.ihl), str(self.dscp), str(self.ecn), str(self.total_length), str(self.identification), str(self.evil_bit), str(self.df), str(self.mf), str(self.fragment_offset), str(self.ttl), str(self.protocol), str(self.checksum), str(self.source_addr), str(self.destination_addr), str(self.options)))
