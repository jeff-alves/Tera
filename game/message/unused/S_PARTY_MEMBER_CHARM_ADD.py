from util.tipo import tipo
class S_PARTY_MEMBER_CHARM_ADD(object):

    def __init__(self, tracker, time, direction, opcode, data):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        server_id = data.read(tipo.uint32)
        player_id = data.read(tipo.uint32)
        id = data.read(tipo.int32)
        duration = data.read(tipo.int32)
        status = data.read(tipo.byte)
