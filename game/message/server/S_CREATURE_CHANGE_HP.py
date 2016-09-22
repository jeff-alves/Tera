class S_CREATURE_CHANGE_HP(object):

    def __init__(self, time, direction, opcode, reader, version):
        HpRemaining = reader.ReadInt32()
        TotalHp = reader.ReadInt32()
        HpChange = reader.ReadInt16()
        Type = reader.ReadInt32()
        Unknow3 = reader.ReadInt16()
        TargetId = reader.ReadEntityId()
        SourceId = reader.ReadEntityId()
        Critical = reader.ReadInt16()
