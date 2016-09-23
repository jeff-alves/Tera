from util import tipo
class S_CREATURE_ROTATE(object):

    def __init__(self, time, direction, opcode, data, version):
        id = data.read(tipo.uint64)
        angle = data.read(tipo.int16)
        delay = data.read(tipo.int16)
