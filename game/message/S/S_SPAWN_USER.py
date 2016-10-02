from util.enums import Category, Race, Gender, PlayerClass
from util.tipo import tipo

class S_SPAWN_USER(object):

    def __init__(self, tracker, time, direction, opcode, data):
        dic = {}
        data.skip(8)
        name_offset = data.read(tipo.offset)
        data.skip(16)
        dic['server_id'] = data.read(tipo.uint32)
        dic['player_id'] = data.read(tipo.uint32)
        id = data.read(tipo.uint64)
        dic['pos'] = data.read(tipo.float, 3)
        dic['angle'] = data.read(tipo.angle) * 360. / 0x10000
        data.skip(4)
        model = data.read(tipo.uint32)
        dic['race'] = Race((model - 100) / 200 % 50)
        dic['gender'] = Gender(model / 100 % 2)
        dic['class'] = PlayerClass(model % 100)
        data.skip(11)
        dic['dead'] = (data.read(tipo.byte) & 1) == 0
        data.poss = name_offset - 4
        dic['name'] = data.read(tipo.string)
        dic['guild_name'] = data.read(tipo.string)
        dic['category'] = Category.User

        tracker.get_entity(id).spaw(dic)
