from util import tipo
class S_DESPAWN_USER(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        id = data.read(tipo.uint64)
        # unk = data.read(tipo.int32)
