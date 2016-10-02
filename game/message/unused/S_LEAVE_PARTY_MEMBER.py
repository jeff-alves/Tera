from util.tipo import tipo
class S_LEAVE_PARTY_MEMBER(object):

    def __init__(self, tracker, time, direction, opcode, data):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        offset = data.read(tipo.uint16)
        server_id = data.read(tipo.uint32)
        player_id = data.read(tipo.uint32)
        name = data.read(tipo.string)
