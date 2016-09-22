from game.player import Player

class C_PLAYER_LOCATION(object):

    def __init__(self, time, direction, opcode, reader, version):
        Position = reader.ReadVector3f()
        Heading = reader.ReadAngle()
        unk1 = reader.ReadInt16()
        Finish = reader.ReadVector3f()
        Ltype = reader.ReadInt32()
        Speed = reader.ReadInt16()
        unk2 = reader.ReadByte()
        TimeStamp = reader.ReadInt32()

        p = Player()
        p.position = Position
        p.heading = Heading
        p.speed = Speed



