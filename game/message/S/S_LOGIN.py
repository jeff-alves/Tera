from util.enums import Race, Gender, PlayerClass, Category
from util.tipo import tipo


class S_LOGIN(object):

    def __init__(self, tracker, time, direction, opcode, data):
        dic = {}
        name_offset = data.read(tipo.offset)
        data.skip(8)
        model = data.read(tipo.uint32)
        dic['race'] = Race((model - 100) / 200 % 50)
        dic['gender'] = Gender(model / 100 % 2)
        dic['class'] = PlayerClass(model % 100)

        id = data.read(tipo.uint64)
        dic['server_id'] = data.read(tipo.uint32)
        dic['player_id'] = data.read(tipo.uint32)
        data.skip(name_offset - 34)
        dic['name'] = data.read(tipo.string)
        dic['category'] = Category.Player

        tracker.player = tracker.get_entity(id)
        tracker.player.login(dic)
