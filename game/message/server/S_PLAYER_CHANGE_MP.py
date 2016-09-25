from util import tipo
class S_PLAYER_CHANGE_MP(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        current_mp = data.read(tipo.int32)
        max_mp = data.read(tipo.int32)
        diff = data.read(tipo.int32)
        typ = data.read(tipo.uint32)
        target = data.read(tipo.uint64)
        source = data.read(tipo.uint64)
