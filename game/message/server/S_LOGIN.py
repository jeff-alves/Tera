class S_LOGIN(object):

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


        nameOffset = reader.ReadInt16()
        reader.Skip(8)
        value = reader.ReadInt32()
        if value / 10000 != 1:
            print("Unexpected raw value for RaceGenderClass")
            return
        Race = RaceEnum[(value - 100) / 200 % 50]
        Gender = GenderEnum[value / 100 % 2]
        Class = PlayerClass[value % 100]

        Id = reader.ReadEntityId()
        ServerId = reader.ReadUInt32()
        PlayerId = reader.ReadUInt32()
        reader.Skip(nameOffset - 34)
        Name = reader.ReadTeraString()
