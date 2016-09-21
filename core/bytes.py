from _struct import unpack
import binascii

class Bytes(bytearray):

    def __init__(self, params=0):
        bytearray.__init__(self, params)
        self.poss = 0

    def __str__(self):
        return str(unpack('!' + (len(self) * 'B'), self))  # [1:-1]

    def __repr__(self):
        return str(unpack('!' + (len(self) * 'B'), self))  # [1:-1]

    def get_bin(self):
        return ''.join([format(b, 'b').zfill(8) for b in unpack('!' + (len(self) * 'B'), self)])

    def read(self, tipo):
        self.poss += tipo[1]
        return unpack('<' + tipo[0], self[self.poss - tipo[1]:self.poss])[0]

    def skip(self, tipo):
        self.poss += tipo[1]

    def get_array(self, tipo):
        return [unpack('!' + tipo[0], self[i:i + tipo[1]]) for i in range(0, len(self), tipo[1])]

    def get_array_int(self, size=4):
        return [int(binascii.b2a_hex(self[i:size + i]), 16) for i in range(0, len(self), size)]

    def len(self):
        return len(self)

