class S_PARTY_MEMBER_CHARM_ADD(object):

    def __init__(self, time, direction, opcode, reader, version):
        ServerId = reader.ReadUInt32()
        PlayerId = reader.ReadUInt32()
        CharmId = reader.ReadUInt32()
        Duration = reader.ReadInt32()
        Status = reader.ReadByte()
