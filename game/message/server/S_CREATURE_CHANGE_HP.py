from util import tipo
class S_CREATURE_CHANGE_HP(object):

    def __init__(self, time, direction, opcode, data, version):
        cur_hp = data.read(tipo.int32)
        max_hp = data.read(tipo.int32)
        diff = data.read(tipo.int32)
        type = data.read(tipo.int32)
        target = data.read(tipo.uint64)
        source = data.read(tipo.uint64)
        crit = data.read(tipo.byte)
