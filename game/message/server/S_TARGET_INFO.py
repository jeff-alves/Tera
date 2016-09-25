from util import tipo
class S_TARGET_INFO(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        data.skip(8)
        target = data.read(tipo.uint64)
