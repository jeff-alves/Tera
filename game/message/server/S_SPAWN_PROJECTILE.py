from util import tipo
class S_SPAWN_PROJECTILE(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        id = data.read(tipo.uint64)
        unk1 = data.read(tipo.int32)
        model = data.read(tipo.int32)
        pos1 = data.read(tipo.float, 3)
        pos2 = data.read(tipo.float, 3)
        unk2 = data.read(tipo.byte)
        speed = data.read(tipo.float)
        source = data.read(tipo.uint64)
        model = data.read(tipo.uint32)
