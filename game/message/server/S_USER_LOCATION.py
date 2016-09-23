from util import tipo
class S_USER_LOCATION(object):

    def __init__(self, time, direction, opcode, data, version):
        target = data.read(tipo.uint64)
        pos1 = data.read(tipo.float, 3)
        angle = data.read(tipo.int16)
        unk2 = data.read(tipo.int16)  # maybe w is int32?
        speed = data.read(tipo.int16)
        pos2 = data.read(tipo.float, 3)
        type = data.read(tipo.int32)
        unk = data.read(tipo.byte)
