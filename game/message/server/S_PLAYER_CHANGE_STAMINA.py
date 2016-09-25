from util import tipo
class S_PLAYER_CHANGE_STAMINA(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        current_re = data.read(tipo.int32)
        max_re = data.read(tipo.int32)
        unk1 = data.read(tipo.int32)
        unk2 = data.read(tipo.int32)
        unk3 = data.read(tipo.int32)
