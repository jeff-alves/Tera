from util import tipo
class S_ABNORMALITY_END(object):

    def __init__(self, time, direction, opcode, data, version):
        target = data.read(tipo.uint64) 
        id = data.read(tipo.uint32) 
