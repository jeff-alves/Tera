from util import tipo
class S_USER_STATUS(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        target = data.read(tipo.uint64)
        status = data.read(tipo.byte)
