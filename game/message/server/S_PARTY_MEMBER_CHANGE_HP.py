class S_PARTY_MEMBER_CHANGE_HP(object):

    def __init__(self, time, direction, opcode, reader, version):
        ServerId = reader.ReadUInt32()
        PlayerId = reader.ReadUInt32()
        HpRemaining = reader.ReadInt32()
        TotalHp = reader.ReadInt32()
        Unknow3 = reader.ReadInt16()
