from util.tipo import tipo
class S_GET_USER_GUILD_LOGO(object):

    def __init__(self, tracker, time, direction, opcode, data):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        offset = data.read(tipo.offset)
        count = data.read(tipo.count)
        player_id = data.read(tipo.int32)
        guild_id = data.read(tipo.int32)
        # logo = data.read(tipo.bytes)
