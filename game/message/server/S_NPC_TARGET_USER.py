from util import tipo
class S_NPC_TARGET_USER(object):

    def __init__(self, time, direction, opcode, data, version):
        target = data.read(tipo.uint64)
        # status = data.read(tipo.byte)
