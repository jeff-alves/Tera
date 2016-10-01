from enum import Enum

class IpProtocol(Enum):
    tcp = 6
    udp = 17

class HitDirection(Enum):
    Back = 1
    Side = 2
    Front = 3
    Dot = 4
    Pet = 5

class Gender(Enum):
    Female = 0
    Male = 1
    Common = 255

class DotType(Enum):
    swch = 0  # switch on for noctineum ? other strange uses.
    seta = 1  # ?set abs stat value
    abs = 2  # each tick  HP +=HPChange ; MP += MPChange
    perc = 3  # each tick  HP += MaxHP*HPChange; MP += MaxMP*MPChange
    setp = 4  # ?set % stat value

class Types(Enum):
    Unknown = 0
    MaxHP = 1
    Power = 3
    Endurance = 4
    MovSpd = 5
    Crit = 6
    CritResist = 7
    ImpactEffective = 8
    Ballance = 9
    WeakResist = 14
    DotResist = 15
    StunResist = 16
    # something strange, internal itemname sleep_protect, but user string is stun resist, russian user string is "control effect resist"
    AllResist = 18
    CritPower = 19
    Aggro = 20
    NoMPDecay = 21  # slayer
    Attack = 22  # total damage modificator
    XPBoost = 23
    ASpd = 24
    MovSpdInCombat = 25
    CraftTime = 26
    OutOfCombatMovSpd = 27
    HPDrain = 28  # drain hp on attack
    # 28 = Something comming with MovSpd debuff skills, fxp 32% MovSpd debuff from Lockdown Blow IV, give also 12% of this kind
    # 29 = something strange when using Lethal Strike
    Stamina = 30
    Gathering = 31
    HPChange = 51
    MPChange = 52
    RageChange = 53
    KnockDownChance = 103
    DefPotion = 104  # or glyph: - incoming damage %
    IncreasedHeal = 105
    PVPDef = 108
    AtkPotion = 162  # or glyph: + outgoing damage %
    CritChance = 167
    PVPAtk = 168
    Noctenium = 203  # different values for different kinds of Noctenium, not sure what for =)
    StaminaDecay = 207
    CDR = 208
    Block = 210  # frontal block ? Not sure, the ability to use block, or blocking stance
    HPLoss = 221  # loss hp at the and of debuff
    Mark = 231  # Velik's Mark/Curse of Kaprima = increase received damage when marked
    CastSpeed = 236
    Range = 259  # increase melee range? method 0 value 0.1= +10%
    # 264 = redirect abnormality, value= new abnormality, bugged due to wrong float format in xml.
    Rage = 280  # tick - RageChange, notick (one change) - Rage
    SuperArmor = 283
    Charm = 65535

class SkillType(Enum):
    Block_dodge = 0
    Atack = 1
    Heal = 2
    Useless = 4

# class SkillResultFlags(Enum):
#     Block_dodge = 0  # test
#     Bit0 = 1  # Usually 1 for attacks, 0 for blocks/dodges but I don't understand its exact semantics yet
#     Heal = 2  # Bit0 == 1 + heal == 1 = mana
#     Bit2 = 4
#     IsDfaResolve = 4
#     Bit16 = 0x10000
#     Bit18 = 0x40000

class PlayerClass(Enum):
    Warrior = 1
    Lancer = 2
    Slayer = 3
    Berserker = 4
    Sorcerer = 5
    Archer = 6
    Priest = 7
    Mystic = 8
    Reaper = 9
    Gunner = 10
    Brawler = 11
    Ninja = 12
    Common = 255

class Race(Enum):
    Human = 0
    Highelf = 1
    Aman = 2
    Castanic = 3
    Popori = 4  # Male=Popori, Female = Elin
    Baraka = 5
    Common = 255

class HotOrDot(Enum):
    Dot = 131071
    Hot = 65536
    #  SystemHot = 655360 # natural regen
    #  CrystalHpHot = 196608  # Not
    #  StuffMpHot = 262144
    #  NaturalMpRegen = 0

class MessageDirection(Enum):
    ClientToServer = 1
    ServerToClient = 2

class BlockType(Enum):
    MagicBytes = 1
    Start = 2
    Timestamp = 3
    Client = 4
    Server = 5
    Region = 6
