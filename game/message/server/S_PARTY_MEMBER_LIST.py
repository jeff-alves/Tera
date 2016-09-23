from util import tipo
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

        count = reader.read(tipo.uint16)
        offset = reader.read(tipo.uint16)
        reader.skip(2)  # ims raid bytes
        reader.skip(12)
        LeaderServerId = reader.read(tipo.uint32)
        LeaderPlayerId = reader.read(tipo.uint32)
        reader.skip(19)
        Party = []
        for i in xrange(1, count + 1):
            reader.skip(4)  # pointer and next member offset
            nameoffset = reader.read(tipo.uint16)
            ServerId = reader.read(tipo.uint32)
            PlayerId = reader.read(tipo.uint32)
            Level = reader.read(tipo.uint32)
            PlayerClass = PlayerClass[reader.read(tipo.int32) + 1]
            Status = reader.read(tipo.byte)
            Id = reader.read(tipo.uint64)
            Order = reader.read(tipo.uint32)
            CanInvite = reader.read(tipo.byte)
            unk1 = reader.read(tipo.uint32)
            Name = reader.ReadTeraString()
            Party.append((ServerId, PlayerId, Level, PlayerClass, Status, Id, Order, CanInvite, unk1, Name))
