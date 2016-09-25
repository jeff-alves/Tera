from util import tipo
class S_END_CHANGE_USER_APPEARANCE(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        ok = data.read(tipo.byte)
        unk = data.read(tipo.byte)
