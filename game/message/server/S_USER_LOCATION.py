class S_USER_LOCATION(object):

    def __init__(self, time, direction, opcode, reader, version):
        Entity = reader.ReadEntityId()
        Start = reader.ReadVector3f()
        Heading = reader.ReadAngle()
        unk1 = reader.ReadInt16()
        Speed = reader.ReadInt16()
        Finish = reader.ReadVector3f()
        Ltype = reader.ReadInt32()
        unk2 = reader.ReadByte()
