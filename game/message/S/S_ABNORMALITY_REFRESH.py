from util.tipo import tipo
class S_ABNORMALITY_REFRESH(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        target = data.read(tipo.uint64)
        abnormality_id = data.read(tipo.uint32)
        duration = data.read(tipo.int32)
        unk = data.read(tipo.int32)
        stacks = data.read(tipo.int32)
