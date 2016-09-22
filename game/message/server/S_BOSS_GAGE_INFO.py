class S_BOSS_GAGE_INFO(object):

    def __init__(self, time, direction, opcode, reader, version):
        EntityId = reader.ReadEntityId()
        Type = reader.ReadInt32()
        NpcId = reader.ReadInt32()
        TargetId = reader.ReadEntityId()
        Unk1 = reader.ReadInt32()
        HpChange = reader.ReadSingle()
        Unk2 = reader.ReadByte()  # enrage?
        HpRemaining = reader.ReadSingle()
        TotalHp = reader.ReadSingle()
