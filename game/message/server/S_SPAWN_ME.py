from util import tipo
class S_SPAWN_ME(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        target = data.read(tipo.uint64)
        pos = data.read(tipo.float, 3)
        angle = data.read(tipo.int16)
        dead = (data.read(tipo.byte) & 1) == 0
        unk = data.read(tipo.byte)
