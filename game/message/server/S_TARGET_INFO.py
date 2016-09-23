from util import tipo
class S_TARGET_INFO(object):

    def __init__(self, time, direction, opcode, data, version):
        data.skip(8)
        target = data.read(tipo.uint64)
