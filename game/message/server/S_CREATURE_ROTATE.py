from util import tipo
class S_CREATURE_ROTATE(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        id = data.read(tipo.uint64)
        angle = data.read(tipo.int16)
        delay = data.read(tipo.int16)
