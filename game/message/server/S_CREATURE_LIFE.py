from util import tipo
class S_CREATURE_LIFE(object):

    def __init__(self, time, direction, opcode, data, version):
        user = data.read(tipo.uint64)
        pos = data.read(tipo.float, 3)
        dead = data.read(tipo.byte) == 0  # 0=dead1=alive
