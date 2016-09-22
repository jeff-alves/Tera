class S_PARTY_MEMBER_CHARM_RESET(object):

    def __init__(self, time, direction, opcode, reader, version):
        count = reader.ReadUInt16()
        offset = reader.ReadUInt16()
        ServerId = reader.ReadUInt32()
        PlayerId = reader.ReadUInt32()
        Charms = []
        for i in xrange(1, count + 1):
            reader.Skip(4)  # offset pointer & next member offset
            charmId = reader.ReadUInt32()
            duration = reader.ReadUInt32()
            status = reader.ReadByte()
            Charms.append((status, charmId, duration))
