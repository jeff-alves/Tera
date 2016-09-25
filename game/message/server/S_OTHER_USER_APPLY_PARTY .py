from util import tipo
class S_OTHER_USER_APPLY_PARTY (object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        data.skip(7)
        clas = data.read(tipo.int16)
        # PlayerClass = (PlayerClass) (clas + 1)
        data.skip(4)
        Lvl = data.read(tipo.int16)
        data.skip(1)
        PlayerName = data.read(tipo.string)
