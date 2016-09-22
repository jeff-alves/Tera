class S_START_USER_PROJECTILE(object):

    def __init__(self, time, direction, opcode, reader, version):
        OwnerId = reader.ReadEntityId()
        reader.Skip(8)
        Id = reader.ReadEntityId()
        SkillId = reader.ReadUInt32()
        Start = reader.ReadVector3f()
        Finish = reader.ReadVector3f()
        Speed = reader.ReadSingle()
