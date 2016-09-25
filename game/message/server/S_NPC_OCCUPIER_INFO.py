from util import tipo
class S_NPC_OCCUPIER_INFO(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        id = data.read(tipo.uint64)
        enraged = data.read(tipo.uint64)
        target = data.read(tipo.uint64)
