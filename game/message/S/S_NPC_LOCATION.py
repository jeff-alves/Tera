from util.tipo import tipo
class S_NPC_LOCATION(object):

    def __init__(self, tracker, time, direction, opcode, data):
        dic = {}
        id = data.read(tipo.uint64)
        dic['pos1'] = data.read(tipo.float, 3)
        dic['angle'] = data.read(tipo.angle) * 360. / 0x10000
        dic['speed'] = data.read(tipo.int16)
        dic['pos'] = data.read(tipo.float, 3)
        dic['type'] = data.read(tipo.int32)  # 0 = Move, 7= Rotate standing

        tracker.get_entity(id).location(dic)
