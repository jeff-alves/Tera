from util import tipo
class S_PLAYER_CHANGE_MP(object):

    def __init__(self, time, direction, opcode, data, version):
        current_mp = data.read(tipo.int32) 
        max_mp = data.read(tipo.int32) 
        diff = data.read(tipo.int32) 
        type = data.read(tipo.uint32) 
        target = data.read(tipo.uint64) 
        source = data.read(tipo.uint64) 
