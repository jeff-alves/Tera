from util.tipo import tipo
class S_ABNORMALITY_END(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        target = data.read(tipo.uint64)
        abnormality_id = data.read(tipo.uint32)
