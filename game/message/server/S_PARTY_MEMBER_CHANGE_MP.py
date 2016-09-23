from util import tipo
class S_PARTY_MEMBER_CHANGE_MP(object):

    def __init__(self, time, direction, opcode, data, version):
        server_id = data.read(tipo.uint32)
        player_id = data.read(tipo.uint32)
        current_mp = data.read(tipo.int32)
        max_mp = data.read(tipo.int32)
        unk1 = data.read(tipo.int16)
