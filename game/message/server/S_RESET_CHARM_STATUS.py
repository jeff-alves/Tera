from util import tipo
class S_RESET_CHARM_STATUS(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        count = data.read(tipo.uint16)
        offset = data.read(tipo.uint16)
        target_id = data.read(tipo.uint64)
        charms = []
        for i in xrange(1, count + 1):
            data.skip(2)  # offset pointer
            data.skip(2)  # next member offset
            charmId = data.read(tipo.uint32)
            duration = data.read(tipo.uint32)
            status = data.read(tipo.byte)
            charms.append(status, charmId, duration)
