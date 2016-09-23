from util import tipo
class S_CHANGE_DESTPOS_PROJECTILE(object):

    def __init__(self, time, direction, opcode, data, version):
        id = data.read(tipo.uint64)
        pos = data.read(tipo.float, 3)
