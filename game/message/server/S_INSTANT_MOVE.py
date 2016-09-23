from util import tipo
class S_INSTANT_MOVE(object):

    def __init__(self, time, direction, opcode, data, version):
        id = data.read(tipo.uint64)
        pos = data.read(tipo.float, 3)
        angle = data.read(tipo.int16)
