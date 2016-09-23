from util import tipo
class S_BOSS_GAGE_INFO(object):

    def __init__(self, time, direction, opcode, data, version):
        id = data.read(tipo.uint64)
        type = data.read(tipo.int32)
        npc = data.read(tipo.int32)
        target = data.read(tipo.uint64)
        unk1 = data.read(tipo.int32)
        hp_diff = data.read(tipo.float)
        unk2 = data.read(tipo.byte)  # enrage?
        cur_hp = data.read(tipo.float)
        max_hp = data.read(tipo.float)