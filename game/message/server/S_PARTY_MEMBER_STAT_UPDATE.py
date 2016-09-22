class S_PARTY_MEMBER_STAT_UPDATE(object):

    def __init__(self, time, direction, opcode, reader, version):
        ServerId = reader.ReadUInt32()
        PlayerId = reader.ReadUInt32()
        HpRemaining = reader.ReadInt32()
        MpRemaining = reader.ReadInt32()
        TotalHp = reader.ReadInt32()
        TotalMp = reader.ReadInt32()
        Level = reader.ReadInt16()
        InCombat = reader.ReadInt16()
        Vitality = reader.ReadInt16()
        Alive = reader.ReadByte()  # not sure
        Stamina = reader.ReadInt32()
        ReRemaining = reader.ReadInt32()
        TotalRe = reader.ReadInt32()
        Unknow3 = reader.ReadInt32()
