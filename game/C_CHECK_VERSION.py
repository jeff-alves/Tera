from util import tipo
class C_CHECK_VERSION(object):

    def __init__(self, msg):
        count = msg[3].read(tipo.uint16)
        offset = msg[3].read(tipo.uint16)
        self.ver = []
        for i in xrange(1, count + 1):
            pointer = msg[3].read(tipo.uint16)
            next_offset = msg[3].read(tipo.uint16)
            version_key = msg[3].read(tipo.uint32)
            version_value = msg[3].read(tipo.uint32)
            self.ver.append((version_key, version_value))
            offset = next_offset
