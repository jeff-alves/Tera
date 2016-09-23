from util import tipo
class S_SPAWN_NPC(object):

    def __init__(self, time, direction, opcode, data, version):
        data.skip(6)
        if version == "KR": data.skip(4)  # not sure what's there
        id = data.read(tipo.uint64)
        target = data.read(tipo.uint64)
        pos = data.read(tipo.float, 3)
        angle = data.read(tipo.int16)
        data.skip(4)
        npc_id = data.read(tipo.uint32)
        npc_area = data.read(tipo.uint16)
        category_id = data.read(tipo.uint32)
        data.skip(31)
        owner_id = data.read(tipo.uint64)