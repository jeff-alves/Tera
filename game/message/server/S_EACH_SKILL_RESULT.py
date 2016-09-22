class S_EACH_SKILL_RESULT(object):

    def __init__(self, time, direction, opcode, reader, version):
        SkillResultFlags = {
            1:'Bit0',  # Usually 1 for attacks, 0 for blocks/dodges but I don't understand its exact semantics yet
            2:'Heal',  # Bit0 == 1 + heal == 1 = mana
            4:'Bit2',
            4:'IsDfaResolve',
            0x10000:'Bit16',
            0x40000:'Bit18'
        }

        reader.Skip(4)
        Source = reader.ReadEntityId()
        if version == "KR": reader.Skip(8)
        Target = reader.ReadEntityId()

        # I think it s some kind of source ID.
        # When I use a skill against any monstrer, it s always the same value
        # When I pick up a mana mote, differente ID
        Unknow1 = reader.ReadBytes(4)

        SkillId = reader.ReadInt32() & 0x3FFFFFF

        # Not sure if it s a int32. or int16 or int64 or other thing
        # When using a skill with many hit, each hit seem to have a different number (ex: 0, 1, 2, or 3)
        HitId = reader.ReadInt32()

        # No fucking idea. I think I see 3 different part in that thing
        Unknow2 = reader.ReadBytes(12)  # unknown, id, time

        Amount = reader.ReadInt32()
        Flags = SkillResultFlags[reader.ReadInt32()]
        IsCritical = (reader.ReadUInt16() & 1) != 0
        Knockdown = (reader.ReadByte() & 1) != 0
        reader.Skip(4)
        Position = reader.ReadVector3f()
        Heading = reader.ReadAngle()
