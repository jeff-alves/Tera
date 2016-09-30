from util.tipo import tipo
class C_START_SKILL(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3] + '(' + str(len(data)) + '): ' + str(data.get_array_hex(1))[1:-1])
        unk1 = data.read(tipo.uint32)
        unk2 = data.read(tipo.uint16)
        pos = data.read(tipo.float, 3)
        unk3 = data.read(tipo.uint64)
        unk4 = data.read(tipo.uint32)

