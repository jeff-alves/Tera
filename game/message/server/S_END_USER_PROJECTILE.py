from util import tipo
class S_END_USER_PROJECTILE(object):

    def __init__(self, time, direction, opcode, data, version):
        id = data.read(tipo.uint64) 
        unk = data.read(tipo.byte) 
