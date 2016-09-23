from util import tipo
class S_NPC_LOCATION(object):

    def __init__(self, time, direction, opcode, data, version):
        target = data.read(tipo.uint64)
        pos1 = data.read(tipo.float, 3)
        angle = data.read(tipo.int16)
        speed = data.read(tipo.int16)
        pos2 = data.read(tipo.float, 3)
        type = data.read(tipo.int32)  # 0 = Move, 7= Rotate standing
