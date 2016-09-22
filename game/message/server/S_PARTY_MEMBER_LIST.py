class S_PARTY_MEMBER_LIST(object):

    def __init__(self, time, direction, opcode, reader, version):
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

        count = reader.ReadUInt16()
        offset = reader.ReadUInt16()
        reader.Skip(2)  # ims raid bytes
        reader.Skip(12)
        LeaderServerId = reader.ReadUInt32()
        LeaderPlayerId = reader.ReadUInt32()
        reader.Skip(19)
        Party = []
        for i in xrange(1, count + 1):
            reader.Skip(4)  # pointer and next member offset
            nameoffset = reader.ReadUInt16()
            ServerId = reader.ReadUInt32()
            PlayerId = reader.ReadUInt32()
            Level = reader.ReadUInt32()
            PlayerClass = PlayerClass[reader.ReadInt32() + 1]
            Status = reader.ReadByte()
            Id = reader.ReadEntityId()
            Order = reader.ReadUInt32()
            CanInvite = reader.ReadByte()
            unk1 = reader.ReadUInt32()
            Name = reader.ReadTeraString()
            Party.append((ServerId, PlayerId, Level, PlayerClass, Status, Id, Order, CanInvite, unk1, Name))
