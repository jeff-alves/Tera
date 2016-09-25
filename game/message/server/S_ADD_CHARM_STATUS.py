from util import tipo
class S_ADD_CHARM_STATUS(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        target = data.read(tipo.uint64)
        id = data.read(tipo.uint32)
        status = data.read(tipo.byte)
        duration = data.read(tipo.int32)
