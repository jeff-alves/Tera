from util import tipo
class S_EACH_SKILL_RESULT(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        SkillResultFlags = {
            1:'Bit0',  # Usually 1 for attacks, 0 for blocks/dodges but I don't understand its exact semantics yet
            2:'Heal',  # Bit0 == 1 + heal == 1 = mana
            4:'Bit2',
            4:'IsDfaResolve',
            0x10000:'Bit16',
            0x40000:'Bit18'
        }

        data.skip(4)
        Source = data.read(tipo.uint64)
        if version == "KR": data.skip(8)
        Target = data.read(tipo.uint64)

        # I think it s some kind of source ID.
        # When I use a skill against any monstrer, it s always the same value
        # When I pick up a mana mote, differente ID
        # Unknow1 = data.ReadBytes(4)
        data.skip(4)

        _SkillId = data.read(tipo.int32)
        SkillId = _SkillId & 0x3FFFFFF

        # Not sure if it s a int32. or int16 or int64 or other thing
        # When using a skill with many hit, each hit seem to have a different number (ex: 0, 1, 2, or 3)
        HitId = data.read(tipo.int32)

        # No fucking idea. I think I see 3 different part in that thing
        # Unknow2 = data.ReadBytes(12)  # unknown, id, time
        data.skip(12)

        Amount = data.read(tipo.int32)
        _Flags = data.read(tipo.int32)
        # Flags = SkillResultFlags[data.read(tipo.int32)]
        IsCritical = (data.read(tipo.uint16) & 1) != 0
        Knockdown = (data.read(tipo.byte) & 1) != 0
        data.skip(4)
        Position = data.read(tipo.float, 3)
        Heading = data.read(tipo.int16)

#     def __init__(self, time, direction, opcode, data, version):
#         count = data.read(tipo.count)
#         offset = data.read(tipo.offset)
#
#         source = data.read(tipo.uint64)
#         if version == "KR": data.skip(8)
#         target = data.read(tipo.uint64)
#
#         model = data.read(tipo.uint32)
#         skill = data.read(tipo.uint32)  # & 0x3FFFFFF
#         stage = data.read(tipo.uint32)
#
#         unk1 = data.read(tipo.int32)
#         id = data.read(tipo.uint32)
#         time = data.read(tipo.int32)
#
#         damage = data.read(tipo.uint32)
#         typ = data.read(tipo.uint16)
#         type2 = data.read(tipo.uint16)
#         crit = data.read(tipo.uint16)
#         knockdown = data.read(tipo.byte)
#         unk2 = data.read(tipo.byte)  # 0..5?
#         unk7 = data.read(tipo.byte)  # bool
#         unk8 = data.read(tipo.byte)  # bool
#         unk9 = data.read(tipo.byte)  # bool
#         pos = data.read(tipo.float, 3)
#         angle = data.read(tipo.int16)
#         # skill2 = data.read(tipo.int32)  # usually 0?
#         # unk4 = data.read(tipo.int32)  # always 0?
#         # attackid = data.read(tipo.int32)
#
#         # unk6
#         # _unk1 = data.read(tipo.int32)
#         # _unk2 = data.read(tipo.float)
#         # _unk3 = data.read(tipo.float)
#         # _unk4 = data.read(tipo.float)
