from util import tipo
class S_REMOVE_CHARM_STATUS(object):

    def __init__(self, time, direction, opcode, data, version):
        id = data.read(tipo.uint32) 