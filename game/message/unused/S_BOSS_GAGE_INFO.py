from util.tipo import tipo
class S_BOSS_GAGE_INFO(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        id = data.read(tipo.uint64)
        typ = data.read(tipo.int32)
        npc = data.read(tipo.int32)
        target = data.read(tipo.uint64)
        unk1 = data.read(tipo.int32)
        hp_diff = data.read(tipo.float)
        unk2 = data.read(tipo.byte)  # enrage?
        cur_hp = data.read(tipo.float)
        max_hp = data.read(tipo.float)
