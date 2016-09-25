from util import tipo
class S_PARTY_MEMBER_ABNORMAL_ADD(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        server_id = data.read(tipo.uint32)
        player_id = data.read(tipo.uint32)
        id = data.read(tipo.int32)
        duration = data.read(tipo.int32)
        stacks = data.read(tipo.int32)
