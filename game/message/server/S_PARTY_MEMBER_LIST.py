from util import tipo
class S_PARTY_MEMBER_LIST(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
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

        count = data.read(tipo.uint16)
        offset = data.read(tipo.uint16)
        data.skip(2)  # ims raid bytes
        data.skip(12)
        LeaderServerId = data.read(tipo.uint32)
        LeaderPlayerId = data.read(tipo.uint32)
        data.skip(19)
        Party = []
        for i in xrange(1, count + 1):
            data.skip(4)  # pointer and next member offset
            nameoffset = data.read(tipo.uint16)
            ServerId = data.read(tipo.uint32)
            PlayerId = data.read(tipo.uint32)
            Level = data.read(tipo.uint32)
            PlayerClass = PlayerClass[data.read(tipo.int32) + 1]
            Status = data.read(tipo.byte)
            Id = data.read(tipo.uint64)
            Order = data.read(tipo.uint32)
            CanInvite = data.read(tipo.byte)
            unk1 = data.read(tipo.uint32)
            Name = data.read(tipo.string)
            Party.append((ServerId, PlayerId, Level, PlayerClass, Status, Id, Order, CanInvite, unk1, Name))
