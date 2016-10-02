from util.enums import DespawnReason
from util.tipo import tipo


class S_DESPAWN_NPC(object):

    def __init__(self, tracker, time, direction, opcode, data):
        dic = {}
        id = data.read(tipo.uint64)
        dic['pos'] = data.read(tipo.float, 3)
        dic['despawn_reason'] = DespawnReason(data.read(tipo.byte))  # 1 = move out of view, 5 = death
        if dic['despawn_reason'] is DespawnReason.Dead: dic['dead'] = True

        tracker.get_entity(id).despawn(dic)
