class S_RESET_CHARM_STATUS(object):

    def __init__(self, time, direction, opcode, reader, version):
        count = reader.ReadUInt16()
        offset = reader.ReadUInt16()
        TargetId = reader.ReadEntityId()
        Charms = []
        for i in xrange(1, count + 1):
            reader.Skip(2)  # offset pointer
            reader.Skip(2)  # next member offset
            charmId = reader.ReadUInt32()
            duration = reader.ReadUInt32()
            status = reader.ReadByte()
            Charms.append(status, charmId, duration)
