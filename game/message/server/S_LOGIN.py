from util import tipo
class S_LOGIN(object):

    def __init__(self, time, direction, opcode, data, version):
        name_offset = data.read(tipo.offset)
        data.skip(8)
#         details_offset = data.read(tipo.offset)
#         details_count = data.read(tipo.count)
#         details2_offset = data.read(tipo.offset)
#         details2_count = data.read(tipo.count)

        model = data.read(tipo.uint32)
        id = data.read(tipo.uint64)
        server_id = data.read(tipo.uint32)
        player_id = data.read(tipo.uint32)

        data.skip(name_offset - 34)
        name = data.read(tipo.string)

#         cid = data.read(tipo.uint64)
#         pid = data.read(tipo.uint64)
#         unk1 = data.read(tipo.int32)
#         unk2 = data.read(tipo.byte)
#         unk3 = data.read(tipo.int32)
#         unk4 = data.read(tipo.int32)
#         unk5 = data.read(tipo.int32)
#         appearance = data.read(tipo.uint64)
#         unk6 = data.read(tipo.int16)
#         level = data.read(tipo.int16)
#         gather_energy = data.read(tipo.int16)
#         gather_unk = data.read(tipo.int16)
#         gather_plants = data.read(tipo.int16)
#         gather_mining = data.read(tipo.int16)
#         unk7 = data.read(tipo.int32)
#         unk8 = data.read(tipo.int32)
#         unk9 = data.read(tipo.int16)
#         exp_total = data.read(tipo.int64)
#         exp_shown = data.read(tipo.int64)
#         exp_needed = data.read(tipo.int64)
#         unk10 = data.read(tipo.int32)
#         unk10b = data.read(tipo.int32)
#         unk10c = data.read(tipo.int32)
#         unk10d = data.read(tipo.int32)
#         rested_current = data.read(tipo.int32)
#         rested_max = data.read(tipo.int32)
#         unk11 = data.read(tipo.float)
#         unk12 = data.read(tipo.int32)
#         weapon = data.read(tipo.int32)
#         chest = data.read(tipo.int32)
#         gloves = data.read(tipo.int32)
#         boots = data.read(tipo.int32)
#         innerwear = data.read(tipo.int32)
#         head = data.read(tipo.int32)
#         face = data.read(tipo.int32)
#         unk13 = data.read(tipo.int32)
#         unk14 = data.read(tipo.int32)
#         unk15 = data.read(tipo.byte)
#         unk16 = data.read(tipo.int32)
#         unk17 = data.read(tipo.int32)
#         title = data.read(tipo.int32)
#         weapon_model = data.read(tipo.int32)
#         chest_model = data.read(tipo.int32)
#         gloves_model = data.read(tipo.int32)
#         boots_model = data.read(tipo.int32)
#         unk19 = data.read(tipo.int32)
#         unk20 = data.read(tipo.int32)
#         unk21 = data.read(tipo.int32)
#         unk22 = data.read(tipo.int32)
#         unk23 = data.read(tipo.int32)
#         unk24 = data.read(tipo.int32)
#         unk25 = data.read(tipo.int32)
#         unk26 = data.read(tipo.int32)
#         weapon_enchantment = data.read(tipo.int32)
#         unk27 = data.read(tipo.int32)
#         unk28 = data.read(tipo.byte)
#         unk29 = data.read(tipo.byte)
#         hair_adornment = data.read(tipo.int32)
#         mask = data.read(tipo.int32)
#         back = data.read(tipo.int32)
#         weapon_skin = data.read(tipo.int32)
#         costume = data.read(tipo.int32)
#         unk30 = data.read(tipo.int32)
#         unk31 = data.read(tipo.int32)
#         unk32 = data.read(tipo.int32)
#         unk33 = data.read(tipo.int32)
#         unk34 = data.read(tipo.byte)
#         unk35 = data.read(tipo.int32)
#         unk36 = data.read(tipo.int32)
#         unk37 = data.read(tipo.int32)
#         unk38 = data.read(tipo.float)
#         unk39 = data.read(tipo.int32)
#         unk40 = data.read(tipo.byte)
#         unk41 = data.read(tipo.int32)
#         name = data.read(tipo.string)
#         details = data.read(tipo.bytes)
#         details2 = data.read(tipo.bytes)