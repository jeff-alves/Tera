from util import tipo
class S_GET_USER_LIST(object):

    def __init__(self, time, direction, opcode, data, version):
        count = data.read(tipo.count)
        offset = data.read(tipo.offset)
        player_guilds = []
        for i in xrange(1, count + 1):
            data.poss = offset - 4
            pointer = data.read(tipo.uint16)
            next_offset = data.read(tipo.uint16)
            data.skip(16)
            player_id = data.read(tipo.uint32)
            data.skip(286)
            guild_id = data.read(tipo.uint32)
            offset = next_offset

            player_guilds.append((player_id, guild_id))
