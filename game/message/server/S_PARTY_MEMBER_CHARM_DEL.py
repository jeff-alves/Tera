class S_PARTY_MEMBER_CHARM_DEL(object):

    def __init__(self, time, direction, opcode, reader, version):
        ServerId = reader.ReadUInt32()
        PlayerId = reader.ReadUInt32()
        CharmId = reader.ReadUInt32()
