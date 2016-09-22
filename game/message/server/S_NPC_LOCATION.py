class S_NPC_LOCATION(object):

    def __init__(self, time, direction, opcode, reader, version):
        Entity = reader.ReadEntityId()
        Start = reader.ReadVector3f()
        Heading = reader.ReadAngle()
        Speed = reader.ReadInt16()
        Finish = reader.ReadVector3f()
        Ltype = reader.ReadInt32()  # 0 = Move, 7= Rotate standing
