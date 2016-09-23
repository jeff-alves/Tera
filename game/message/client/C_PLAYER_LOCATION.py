from game.trackers.player import Player
from util import tipo


class C_PLAYER_LOCATION(object):

    def __init__(self, time, direction, opcode, data, version):
        pos1 = data.read(tipo.float, 3)
        angle = data.read(tipo.int16)
        unk1 = data.read(tipo.int16)  # maybe is int32?
        pos2 = data.read(tipo.float, 3)
        type = data.read(tipo.int32)
        speed = data.read(tipo.int16)
        unk2 = data.read(tipo.byte)
        time = data.read(tipo.int32)

        Player().event_pos(pos1, pos2, angle, speed)
