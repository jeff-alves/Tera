# from game.message.client import *
from core.bytes import Bytes
from game.message.server.S_PLAYER_CHANGE_MP import S_PLAYER_CHANGE_MP


# from game.message.server import *
if __name__ == '__main__':
    a = Bytes([113, 14, 0, 0, 113, 14, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 93, 86, 164, 15, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    # S_PLAYER_CHANGE_MP(None, None, None, a, None)
    print(a)
    print(a.ReadInt32())
    print(a.ReadInt32())
    print(a.ReadInt16())
    print(a.ReadInt32())
    print(a.ReadInt16())
    print(a.ReadEntityId())
    print(a.ReadEntityId())
    print(a.ReadInt16())
