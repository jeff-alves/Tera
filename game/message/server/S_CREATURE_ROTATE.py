class S_CREATURE_ROTATE(object):

    def __init__(self, time, direction, opcode, reader, version):
        Entity = reader.ReadEntityId()
        Heading = reader.ReadAngle()
        NeedTime = reader.ReadInt16()
