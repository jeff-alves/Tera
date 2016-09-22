class S_ACTION_STAGE(object):

    def __init__(self, time, direction, opcode, reader, version):
        reader.Skip(4)
        Entity = reader.ReadEntityId()
        Position = reader.ReadVector3f()
        Heading = reader.ReadAngle()
        Model = reader.ReadUInt32()
        SkillId = reader.ReadInt32() & 0x3FFFFFF
        Stage = reader.ReadUInt32()
        Speed = reader.ReadSingle()
        Id = reader.ReadUInt32()
        unk = reader.ReadSingle()
