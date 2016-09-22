class S_ACTION_END(object):

    def __init__(self, time, direction, opcode, reader, version):
        Entity = reader.ReadEntityId()
        Position = reader.ReadVector3f()
        Heading = reader.ReadAngle()
        Model = reader.ReadUInt32()
        SkillId = reader.ReadInt32() & 0x3FFFFFF
        unk = reader.ReadInt32()
        Id = reader.ReadUInt32()

