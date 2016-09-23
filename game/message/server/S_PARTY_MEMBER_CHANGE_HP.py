from util import tipo
class S_PARTY_MEMBER_CHANGE_HP(object):

    def __init__(self, time, direction, opcode, data, version):
        server_id = data.read(tipo.uint32)
        player_id = data.read(tipo.uint32)
        current_hp = data.read(tipo.int32)
        max_hp = data.read(tipo.int32)
        unk1 = data.read(tipo.int16)
