from util import tipo
class S_PARTY_MEMBER_ABNORMAL_ADD(object):

    def __init__(self, time, direction, opcode, data, version):
        server_id = data.read(tipo.uint32)
        player_id = data.read(tipo.uint32)
        id = data.read(tipo.int32)
        duration = data.read(tipo.int32)
        stacks = data.read(tipo.int32)