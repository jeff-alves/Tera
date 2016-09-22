class S_ADD_CHARM_STATUS(object):

    def __init__(self, time, direction, opcode, reader, version):
        TargetId = reader.ReadEntityId()
        CharmId = reader.ReadUInt32()
        Status = reader.ReadByte()
        Duration = reader.ReadInt32()
