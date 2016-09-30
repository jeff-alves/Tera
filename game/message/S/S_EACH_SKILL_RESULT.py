from util.enums import SkillResultFlags
from util.tipo import tipo


class S_EACH_SKILL_RESULT(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        data.skip(4)
        source = data.read(tipo.uint64)
        if version == "KR": data.skip(8)
        target = data.read(tipo.uint64)

        # I think it s some kind of source ID.
        # When I use a skill against any monstrer, it s always the same value
        # When I pick up a mana mote, differente ID
        unk1 = data.read(tipo.uint32)

        skill_id = data.read(tipo.int32) & 0x3FFFFFF

        # Not sure if it s a int32. or int16 or int64 or other thing
        # When using a skill with many hit, each hit seem to have a different number (ex: 0, 1, 2, or 3)
        hit_id = data.read(tipo.int32)

        # No fucking idea. I think I see 3 different part in that thing
        data.skip(12)  # unknown, id, time

        amount = data.read(tipo.int32)
        flags = SkillResultFlags(data.read(tipo.int32))
        is_critical = (data.read(tipo.uint16) & 1) != 0
        knockdown = (data.read(tipo.byte) & 1) != 0
        data.skip(4)
        position = data.read(tipo.float, 3)
        angle = data.read(tipo.angle) * 360. / 0x10000
