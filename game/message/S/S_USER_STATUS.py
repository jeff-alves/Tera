from util.tipo import tipo
class S_USER_STATUS(object):

    def __init__(self, tracker, time, direction, opcode, data):
        dic = {}
        id = data.read(tipo.uint64)
        dic['in_battle'] = data.read(tipo.byte)

        tracker.get_entity(id).status(dic)
