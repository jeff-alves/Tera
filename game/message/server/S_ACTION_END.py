from util import tipo
class S_ACTION_END(object):

    def __init__(self, time, direction, opcode, data, version):
        source = data.read(tipo.uint64)
        pos = data.read(tipo.float, 3)
        angle = data.read(tipo.int16)
        model = data.read(tipo.uint32)
        skill = data.read(tipo.uint32)  # & 0x3FFFFFF
        unk = data.read(tipo.int32)
        id = data.read(tipo.uint32)
