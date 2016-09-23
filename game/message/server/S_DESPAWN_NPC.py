from util import tipo
class S_DESPAWN_NPC(object):

    def __init__(self, time, direction, opcode, data, version):
        id = data.read(tipo.uint64)
        pos = data.read(tipo.float, 3)
        dead = data.read(tipo.byte)  # 1 = move out of view, 5 = death
        # type = data.read(tipo.int32)
        # unk = data.read(tipo.int32)
