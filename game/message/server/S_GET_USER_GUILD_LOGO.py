from util import tipo
class S_GET_USER_GUILD_LOGO(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        offset = data.read(tipo.offset)
        count = data.read(tipo.count)
        player_id = data.read(tipo.int32)
        guild_id = data.read(tipo.int32)
        # logo = data.read(tipo.bytes)
