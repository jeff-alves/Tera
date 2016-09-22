class S_PARTY_MEMBER_CHANGE_MP(object):

    def __init__(self, time, direction, opcode, reader, version):
        ServerId = reader.ReadUInt32()
        PlayerId = reader.ReadUInt32()
        MpRemaining = reader.ReadInt32()
        TotalMp = reader.ReadInt32()
        Unknow3 = reader.ReadInt16()
