from util.tipo import tipo
class S_DESPAWN_USER(object):

    def __init__(self, tracker, time, direction, opcode, data):
        dic = {}
        id = data.read(tipo.uint64)

        tracker.get_entity(id).despawn(dic)
