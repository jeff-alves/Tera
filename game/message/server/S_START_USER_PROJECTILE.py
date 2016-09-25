from util import tipo
class S_START_USER_PROJECTILE(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        source = data.read(tipo.uint64)
        model = data.read(tipo.uint32)
        unk = data.read(tipo.int32)
        id = data.read(tipo.uint64)
        skill = data.read(tipo.uint32)
        pos1 = data.read(tipo.float, 3)
        pos2 = data.read(tipo.float, 3)
        speed = data.read(tipo.float)
