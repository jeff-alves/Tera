from util import tipo
class S_GET_USER_GUILD_LOGO(object):

    def __init__(self, time, direction, opcode, data, version):
        offset = data.read(tipo.offset)
        count = data.read(tipo.count)
        player_id = data.read(tipo.int32)
        guild_id = data.read(tipo.int32)
        # logo = data.read(tipo.bytes)
