from util import tipo
class S_ABNORMALITY_REFRESH(object):

    def __init__(self, time, direction, opcode, data, version):
        target = data.read(tipo.uint64) 
        id = data.read(tipo.uint32) 
        duration = data.read(tipo.int32) 
        unk = data.read(tipo.int32) 
        stacks = data.read(tipo.int32) 
