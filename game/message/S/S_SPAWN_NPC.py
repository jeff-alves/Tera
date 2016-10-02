from game.services.npc_database import NpcDatabase
from game.services.server_database import ServerDatabase
from util.enums import Category
from util.tipo import tipo


class S_SPAWN_NPC(object):

    def __init__(self, tracker, time, direction, opcode, data):
        dic = {}
        data.skip(6)
        if ServerDatabase().selected['location'] == "KR": data.skip(4)  # not sure what's there
        id = data.read(tipo.uint64)
        dic['target'] = data.read(tipo.uint64)
        dic['pos'] = data.read(tipo.float, 3)
        dic['angle'] = data.read(tipo.angle) * 360. / 0x10000
        data.skip(4)
        npc_id = data.read(tipo.uint32)
        npc_area = data.read(tipo.uint16)
        dic['category_id'] = data.read(tipo.uint32)
        data.skip(31)
        dic['owner_id'] = data.read(tipo.uint64)
        dic['category'] = Category.NPC
        dic.update(NpcDatabase().get((npc_area, npc_id), {'npc_area':npc_area, 'npc_id':npc_id}))

        tracker.get_entity(id).spaw(dic)
