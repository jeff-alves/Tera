from util import tipo
class S_PARTY_MEMBER_STAT_UPDATE(object):

    def __init__(self, time, direction, opcode, data, version):
        server_id = data.read(tipo.uint32)
        player_id = data.read(tipo.uint32)
        cur_hp = data.read(tipo.int32)
        cur_mp = data.read(tipo.int32)
        max_hp = data.read(tipo.int32)
        max_mp = data.read(tipo.int32)
        level = data.read(tipo.int16)
        in_combat = data.read(tipo.int16)
        vitality = data.read(tipo.int16)
        alive = data.read(tipo.byte)  # ?
        stamina = data.read(tipo.int32)
        cur_re = data.read(tipo.int32)
        max_re = data.read(tipo.int32)
        unk2 = data.read(tipo.int32)
