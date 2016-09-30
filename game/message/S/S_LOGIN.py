from util.enums import Race, Gender, PlayerClass
from util.tipo import tipo


class S_LOGIN(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        name_offset = data.read(tipo.offset)
        data.skip(8)
        model = data.read(tipo.uint32)
        race = Race((model - 100) / 200 % 50)
        gender = Gender(model / 100 % 2)
        classe = PlayerClass(model % 100)

        id = data.read(tipo.uint64)
        server_id = data.read(tipo.uint32)
        player_id = data.read(tipo.uint32)
        data.skip(name_offset - 34)
        name = data.read(tipo.string)

        tracker.player.login(name, race, gender, classe, id, server_id, player_id)
