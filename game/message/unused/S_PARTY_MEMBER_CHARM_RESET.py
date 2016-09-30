from util.tipo import tipo
class S_PARTY_MEMBER_CHARM_RESET(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
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
