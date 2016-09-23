from util import tipo
class S_PLAYER_CHANGE_STAMINA(object):

    def __init__(self, time, direction, opcode, data, version):
        current_re = data.read(tipo.int32)
        max_re = data.read(tipo.int32)
        unk1 = data.read(tipo.int32)
        unk2 = data.read(tipo.int32)
        unk3 = data.read(tipo.int32)
