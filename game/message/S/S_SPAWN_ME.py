from util.tipo import tipo
class S_SPAWN_ME(object):

    def __init__(self, tracker, time, direction, opcode, data):
        dic = {}
        dic['target'] = data.read(tipo.uint64)
        dic['pos'] = data.read(tipo.float, 3)
        dic['angle'] = data.read(tipo.angle) * 360. / 0x10000
        dic['dead'] = (data.read(tipo.byte) & 1) == 0
        unk = data.read(tipo.byte)

        tracker.player.dic.update(dic)
