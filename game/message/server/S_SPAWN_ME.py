class S_SPAWN_ME(object):

    def __init__(self, time, direction, opcode, reader, version):
        Id = reader.ReadEntityId()
        Position = reader.ReadVector3f()
        Heading = reader.ReadAngle()
        Dead = (reader.ReadByte() & 1) == 0
        unk1 = reader.ReadByte()
