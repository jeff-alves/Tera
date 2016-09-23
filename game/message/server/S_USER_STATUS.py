from util import tipo
class S_USER_STATUS(object):

    def __init__(self, time, direction, opcode, data, version):
        target = data.read(tipo.uint64)
        status = data.read(tipo.byte)
