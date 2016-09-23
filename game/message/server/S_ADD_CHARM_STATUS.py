from util import tipo
class S_ADD_CHARM_STATUS(object):

    def __init__(self, time, direction, opcode, data, version):
        target = data.read(tipo.uint64) 
        id = data.read(tipo.uint32) 
        status = data.read(tipo.byte) 
        duration = data.read(tipo.int32) 
