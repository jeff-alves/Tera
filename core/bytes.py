from _struct import unpack
import binascii
from util.tipo import tipo

class Bytes(bytearray):

    def __init__(self, params=0):
        bytearray.__init__(self, params)
        self.poss = 0

    # def __str__(self):
        # return str(unpack('!' + (len(self) * 'B'), self))  # [1:-1]

    # def __repr__(self):
        # return str(unpack('!' + (len(self) * 'B'), self))  # [1:-1]

    def get_bin(self):
        return ''.join([format(b, 'b').zfill(8) for b in unpack('!' + (len(self) * 'B'), self)])

#------------------------------------------------------
    def read(self, tp, qty=1):
        if tp == tipo.string:
            sep = '\0\0\0'
            i = self.poss
            self.poss += self[self.poss:].find(sep) + len(sep)
            return str(Bytes(filter(lambda a: a != 0, self[i:self.poss - len(sep)])))
        else:
            self.poss += (tp[1] * qty)
            r = unpack('<' + (tp[0] * qty), self[self.poss - (tp[1] * qty):self.poss])
            return r if qty > 1 else r[0]


    def skip(self, qty):
        self.poss += qty
#------------------------------------------------------

    def get_array(self, tipo):
        return [unpack('!' + tipo[0], self[i:i + tipo[1]]) for i in range(0, len(self), tipo[1])]

    def get_array_int(self, size=4):
        return [int(binascii.b2a_hex(self[i:size + i]), 16) for i in range(0, len(self), size)]

    def get_array_hex(self, size=4):
        return [binascii.b2a_hex(self[i:size + i]) for i in range(0, len(self), size)]

    def len(self):
        return len(self)

