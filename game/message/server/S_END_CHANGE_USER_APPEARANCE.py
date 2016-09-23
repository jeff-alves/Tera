from util import tipo
class S_END_CHANGE_USER_APPEARANCE(object):

    def __init__(self, time, direction, opcode, data, version):
        ok = data.read(tipo.byte) 
        unk = data.read(tipo.byte) 
