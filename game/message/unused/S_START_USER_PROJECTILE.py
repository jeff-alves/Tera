from util.tipo import tipo
class S_START_USER_PROJECTILE(object):

    def __init__(self, tracker, time, direction, opcode, data):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        source = data.read(tipo.uint64)
        model = data.read(tipo.uint32)
        unk = data.read(tipo.int32)
        id = data.read(tipo.uint64)
        skill = data.read(tipo.uint32)
        pos1 = data.read(tipo.float, 3)
        pos2 = data.read(tipo.float, 3)
        speed = data.read(tipo.float)
