class S_INSTANT_MOVE(object):

    def __init__(self, time, direction, opcode, reader, version):
        Entity = reader.ReadEntityId()
        Position = reader.ReadVector3f()
        Heading = reader.ReadAngle()
