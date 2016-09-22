class S_SPAWN_NPC(object):

    def __init__(self, time, direction, opcode, reader, version):
        reader.Skip(6)
        if version == "KR": reader.Skip(4)  # not sure what's there
        Id = reader.ReadEntityId()
        TargetId = reader.ReadEntityId()
        Position = reader.ReadVector3f()
        Heading = reader.ReadAngle()
        reader.Skip(4)
        NpcId = reader.ReadUInt32()
        NpcArea = reader.ReadUInt16()
        CategoryId = reader.ReadUInt32()
        reader.Skip(31)
        OwnerId = reader.ReadEntityId()
