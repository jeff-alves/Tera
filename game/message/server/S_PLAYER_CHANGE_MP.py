class S_PLAYER_CHANGE_MP(object):

    def __init__(self, time, direction, opcode, reader, version):
        MpRemaining = reader.ReadInt32()
        TotalMp = reader.ReadInt32()
        MpChange = reader.ReadInt16()
        Type = reader.ReadInt32()
        Unknow3 = reader.ReadInt16()
        TargetId = reader.ReadEntityId()
        SourceId = reader.ReadEntityId()
        Critical = reader.ReadInt16()
