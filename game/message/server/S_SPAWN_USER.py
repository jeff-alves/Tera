class S_SPAWN_USER(object):

    def __init__(self, time, direction, opcode, reader, version):
        RaceEnum = {
            0:'Human',
            1:'Highelf',
            2:'Aman',
            3:'Castanic',
            4:'Popori',
            5:'Baraka',

            255:'Common'
        }

        GenderEnum = {
            0:'Female',
            1:'Male',

            255:'Common'
        }

        PlayerClass = {
            1:'Warrior',
            2:'Lancer',
            3:'Slayer',
            4:'Berserker',
            5:'Sorcerer',
            6:'Archer',
            7:'Priest',
            8:'Mystic',
            9:'Reaper',
            10:'Gunner',
            11:'Brawler',
            12:'Ninja',

            255:'Common'
        }

        reader.Skip(8)
        nameOffset = reader.ReadUInt16()
        reader.Skip(16)
        ServerId = reader.ReadUInt32()
        # not sure, whether full uint32 is serverid, or only first 2 bytes and the rest part of it is actualy a part of PlayerId, or something else, but it always come along with PlayerID as complex player id
        PlayerId = reader.ReadUInt32()
        Id = reader.ReadEntityId()
        Position = reader.ReadVector3f()
        Heading = reader.ReadAngle()
        reader.Skip(4)
        value = reader.ReadInt32()
        if value / 10000 != 1:
            print("Unexpected raw value for RaceGenderClass")
            return
        Race = RaceEnum[(value - 100) / 200 % 50]
        Gender = GenderEnum[value / 100 % 2]
        Class = PlayerClass[value % 100]
        reader.Skip(11)
        Dead = (reader.ReadByte() & 1) == 0
        # reader.BaseStream.Position = nameOffset - 4
        Name = reader.ReadTeraString()
        GuildName = reader.ReadTeraString()
