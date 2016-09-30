from util.tipo import tipo
class S_GET_USER_LIST(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
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
