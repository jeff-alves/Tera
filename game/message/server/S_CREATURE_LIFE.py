class S_CREATURE_LIFE(object):

    def __init__(self, time, direction, opcode, reader, version):
        User = reader.ReadEntityId()
        Position = reader.ReadVector3f()
        Dead = reader.ReadByte() == 0  # 0=dead1=alive
