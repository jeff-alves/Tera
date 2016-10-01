from game.services.skill_database import SkillDatabase
from util.enums import SkillType
from util.tipo import tipo


class S_EACH_SKILL_RESULT(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        dic = {}
        data.skip(4)
        dic['source'] = data.read(tipo.uint64)
        if version == "KR": data.skip(8)
        dic['target'] = data.read(tipo.uint64)
        # I think it s some kind of source ID.
        # When I use a skill against any monstrer, it s always the same value
        # When I pick up a mana mote, differente ID
        unk1 = data.read(tipo.uint32)
        dic['skill_id'] = data.read(tipo.int32) & 0x3FFFFFF
        # Not sure if it s a int32. or int16 or int64 or other thing
        # When using a skill with many hit, each hit seem to have a different number (ex: 0, 1, 2, or 3)
        dic['hit_id'] = data.read(tipo.int32)
        # No fucking idea. I think I see 3 different part in that thing
        data.skip(12)  # unknown, id, time
        dic['amount'] = data.read(tipo.int32)
        dic['type'] = SkillType(data.read(tipo.int32))
        dic['is_critical'] = (data.read(tipo.uint16) & 1) != 0
        dic['knockdown'] = (data.read(tipo.byte) & 1) != 0
        data.skip(4)
        dic['position'] = data.read(tipo.float, 3)
        dic['angle'] = data.read(tipo.angle) * 360. / 0x10000

        print('---------------------------')
        player = tracker.player.dic
        if dic['source'] == player.get('id'):
            skill = SkillDatabase().get((dic['skill_id'], player['class']))
            print(player)
            print(skill)
            print(dic)
        else:
            print(dic)
        print('---------------------------')

