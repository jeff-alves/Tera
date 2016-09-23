from util import tipo
class C_CHECK_VERSION(object):

    def __init__(self, time, direction, opcode, data, version):
        count = data.read(tipo.count)
        offset = data.read(tipo.offset)
        self.ver = []
        for i in xrange(1, count + 1):
            data.poss = offset - 4
            pointer = data.read(tipo.int16)
            next_offset = data.read(tipo.uint16)
            index = data.read(tipo.int32)
            value = data.read(tipo.int32)
            offset = next_offset
            self.ver.append((index, value))
