from util import tipo
class S_LEAVE_PARTY_MEMBER(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        offset = data.read(tipo.uint16)
        server_id = data.read(tipo.uint32)
        player_id = data.read(tipo.uint32)
        name = data.read(tipo.string)
