from util.enums import PlayerClass
from util.tipo import tipo


class S_PARTY_MEMBER_LIST(object):

    def __init__(self, tracker, time, direction, opcode, data):
        dic = {}
        count = data.read(tipo.uint16)
        offset = data.read(tipo.uint16)
        data.skip(2)  # ims raid bytes
        data.skip(12)
        dic['leader_server_id'] = data.read(tipo.uint32)
        dic['leader_player_id'] = data.read(tipo.uint32)
        data.skip(19)
        for i in xrange(1, count + 1):
            dic2 = {}
            data.skip(4)  # pointer and next member offset
            nameoffset = data.read(tipo.uint16)
            dic2['server_id'] = data.read(tipo.uint32)
            dic2['player_id'] = data.read(tipo.uint32)
            dic2['level'] = data.read(tipo.uint32)
            dic2['player_class'] = PlayerClass[data.read(tipo.int32) + 1]
            dic2['status'] = data.read(tipo.byte)
            dic2['id'] = data.read(tipo.uint64)
            dic2['order'] = data.read(tipo.uint32)
            dic2['can_invite'] = data.read(tipo.byte)
            unk1 = data.read(tipo.uint32)
            dic2['name'] = data.read(tipo.string)

            dic[dic2['player_id']] = dic2

        tracker.party.list(dic)
