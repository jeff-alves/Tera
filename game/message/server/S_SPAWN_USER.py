from util import tipo
class S_SPAWN_USER(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        data.skip(8)
        name_offset = data.read(tipo.offset)
        data.skip(16)
        server_id = data.read(tipo.uint32)
        player_id = data.read(tipo.uint32)
        id = data.read(tipo.uint64)
        pos = data.read(tipo.float, 3)
        angle = data.read(tipo.int16)
        data.skip(4)
        model = data.read(tipo.int32)
        data.skip(11)
        dead = (data.read(tipo.byte) & 1) == 0
        data.poss = name_offset - 4
        name = data.read(tipo.string)
        guild_name = data.read(tipo.string)
