from util.tipo import tipo
class S_PLAYER_CHANGE_MP(object):

    def __init__(self, tracker, time, direction, opcode, data):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        current_mp = data.read(tipo.int32)
        max_mp = data.read(tipo.int32)
        diff = data.read(tipo.int32)
        typ = data.read(tipo.uint32)
        target = data.read(tipo.uint64)
        source = data.read(tipo.uint64)
