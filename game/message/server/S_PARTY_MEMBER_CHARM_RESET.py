from util import tipo
class S_PARTY_MEMBER_CHARM_RESET(object):

    def __init__(self, time, direction, opcode, data, version):
        count = data.read(tipo.uint16)
        offset = data.read(tipo.uint16)
        server_id = data.read(tipo.uint32)
        player_id = data.read(tipo.uint32)
        charms = []
        for i in xrange(1, count + 1):
            data.skip(4)  # offset pointer & next member offset
            charm_id = data.read(tipo.uint32)
            duration = data.read(tipo.uint32)
            status = data.read(tipo.byte)
            charms.append((status, charm_id, duration))
