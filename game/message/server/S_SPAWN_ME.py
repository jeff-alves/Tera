from util import tipo
class S_SPAWN_ME(object):

    def __init__(self, time, direction, opcode, data, version):
        target = data.read(tipo.uint64)
        pos = data.read(tipo.float, 3)
        angle = data.read(tipo.int16)
        dead = (data.read(tipo.byte) & 1) == 0
        unk = data.read(tipo.byte)
