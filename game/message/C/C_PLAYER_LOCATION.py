from util.tipo import tipo


class C_PLAYER_LOCATION(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        dic = {}
        dic['pos1'] = data.read(tipo.float, 3)
        dic['angle'] = data.read(tipo.angle) * 360. / 0x10000
        dic['unk1'] = data.read(tipo.int16)  # maybe is int32?
        dic['pos2'] = data.read(tipo.float, 3)
        dic['type'] = data.read(tipo.int32)
        dic['speed'] = data.read(tipo.int16)
        dic['unk2'] = data.read(tipo.byte)
        dic['time'] = data.read(tipo.int32)

        tracker.player.pos(dic)
