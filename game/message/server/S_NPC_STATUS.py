from util import tipo
class S_NPC_STATUS(object):

    def __init__(self, time, direction, opcode, data, version):
        id = data.read(tipo.uint64)
        enraged = data.read(tipo.byte)  # & 1
        unk1 = data.read(tipo.int32)
        target = data.read(tipo.uint64)
        unk2 = data.read(tipo.int32)
