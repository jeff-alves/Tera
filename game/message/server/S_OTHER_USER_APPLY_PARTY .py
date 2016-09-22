class S_OTHER_USER_APPLY_PARTY (object):

    def __init__(self, time, direction, opcode, reader, version):
        reader.Skip(7)
        clas = reader.ReadInt16()
        PlayerClass = (PlayerClass) (clas + 1)
        reader.Skip(4)
        Lvl = reader.ReadInt16()
        reader.Skip(1)
        PlayerName = reader.ReadTeraString()
