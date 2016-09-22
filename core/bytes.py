from _struct import unpack
import binascii
from util import tipo

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

#------------------------------------------------------
    def ReadEntityId(self):
        return self.read(tipo.ulonglong64)

    def ReadVector3f(self):
        return (self.read(tipo.float32), self.read(tipo.float32), self.read(tipo.float32))

    def ReadAngle(self):
        return self.read(tipo.int16)

    def ReadUInt16(self):
        return self.read(tipo.uint16)

    def ReadUInt32(self):
        return self.read(tipo.uint32)

    def ReadUInt64(self):
        return self.read(tipo.ulonglong64)

    def ReadInt16(self):
        return self.read(tipo.int16)

    def ReadInt32(self):
        return self.read(tipo.int32)

    def ReadInt64(self):
        return self.read(tipo.longlong64)

    def ReadByte(self):
        return self.read(tipo.uint8)

    def ReadBytes(self, b):
        self.poss += b
        return self[self.poss - b:self.poss]

    def ReadSingle(self):
        return self.read(tipo.float32)

    def ReadTeraString(self):
        end = self[self.poss:].find('\0') + 1
        self.poss += end
        return self[self.poss - end:self.poss - 1]

    def Skip(self, b):
        self.poss += b
#------------------------------------------------------

    def get_array(self, tipo):
        return [unpack('!' + tipo[0], self[i:i + tipo[1]]) for i in range(0, len(self), tipo[1])]

    def get_array_int(self, size=4):
        return [int(binascii.b2a_hex(self[i:size + i]), 16) for i in range(0, len(self), size)]

    def len(self):
        return len(self)

