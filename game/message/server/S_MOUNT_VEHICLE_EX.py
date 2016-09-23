from util import tipo
class S_MOUNT_VEHICLE_EX(object):

    def __init__(self, time, direction, opcode, data, version):
        owner = data.read(tipo.uint64)
        id = data.read(tipo.uint64)
