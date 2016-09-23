from util import tipo
class S_DESPAWN_USER(object):

    def __init__(self, time, direction, opcode, data, version):
        id = data.read(tipo.uint64)
        # unk = data.read(tipo.int32)
