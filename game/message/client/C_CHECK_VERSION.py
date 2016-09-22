from util import tipo
class C_CHECK_VERSION(object):

    def __init__(self, time, direction, opcode, reader, version):
        count = reader.read(tipo.uint16)
        offset = reader.read(tipo.uint16)
        self.ver = []
        for i in xrange(1, count + 1):
            pointer = reader.read(tipo.uint16)
            next_offset = reader.read(tipo.uint16)
            version_key = reader.read(tipo.uint32)
            version_value = reader.read(tipo.uint32)
            self.ver.append((version_key, version_value))
            offset = next_offset
