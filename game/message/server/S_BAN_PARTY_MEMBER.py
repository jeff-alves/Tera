from util import tipo
class S_BAN_PARTY_MEMBER(object):

    def __init__(self, time, direction, opcode, data, version):
        offset = data.read(tipo.uint16)
        server_id = data.read(tipo.uint32)
        player_id = data.read(tipo.uint32)
        data.skip(4)  # unknown ffffffff
        name = data.read(tipo.string)

