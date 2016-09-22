class S_SPAWN_PROJECTILE(object):

    def __init__(self, time, direction, opcode, reader, version):
        Id = reader.ReadEntityId()
        reader.Skip(4)
        Model = reader.ReadInt32()
        Start = reader.ReadVector3f()
        Finish = reader.ReadVector3f()
        unk1 = reader.ReadByte()
        Speed = reader.ReadSingle()
        OwnerId = reader.ReadEntityId()
        unk2 = reader.ReadInt16()
