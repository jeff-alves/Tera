from util.tipo import tipo
class S_PLAYER_STAT_UPDATE(object):

    def __init__(self, tracker, time, direction, opcode, data):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        HpRemaining = data.read(tipo.int32)
        MpRemaining = data.read(tipo.int32)
        data.skip(4)
        TotalHp = data.read(tipo.int32)
        TotalMp = data.read(tipo.int32)
        return  # we don't need all other things now, but if we need - just remove return.
        BasePower = data.read(tipo.int32)
        BaseEndurance = data.read(tipo.int32)
        BaseImpactFactor = data.read(tipo.int32)
        BaseBalanceFactor = data.read(tipo.int32)
        BaseMovementSpeed = data.read(tipo.int16)
        data.skip(2)
        BaseAttackSpeed = data.read(tipo.int16)
        BaseCritRate = data.read(tipo.float)
        BaseCritResist = data.read(tipo.float)
        BaseCritPower = data.read(tipo.float)
        BaseAttack = data.read(tipo.int32)
        BaseAttack2 = data.read(tipo.int32)
        BaseDefence = data.read(tipo.int32)
        BaseImpcat = data.read(tipo.int32)
        BaseBalance = data.read(tipo.int32)
        BaseResistWeakening = data.read(tipo.float)
        BaseResistPeriodic = data.read(tipo.float)
        BaseResistStun = data.read(tipo.float)
        BonusPower = data.read(tipo.int32)
        BonusEndurance = data.read(tipo.int32)
        BonusImpactFactor = data.read(tipo.int32)
        BonusBalanceFactor = data.read(tipo.int32)
        BonusMovementSpeed = data.read(tipo.int16)
        data.skip(2)
        BonusAttackSpeed = data.read(tipo.int16)
        BonusCritRate = data.read(tipo.float)
        BonusCritResist = data.read(tipo.float)
        BonusCritPower = data.read(tipo.float)
        BonusAttack = data.read(tipo.int32)
        BonusAttack2 = data.read(tipo.int32)
        BonusDefence = data.read(tipo.int32)
        BonusImpcat = data.read(tipo.int32)
        BonusBalance = data.read(tipo.int32)
        BonusResistWeakening = data.read(tipo.float)
        BonusResistPeriodic = data.read(tipo.float)
        BonusResistStun = data.read(tipo.float)
        Level = data.read(tipo.int32)
        Vitality = data.read(tipo.int16)
        Status = data.read(tipo.byte)
        BonusHp = data.read(tipo.int32)
        BonusMp = data.read(tipo.int32)
        Stamina = data.read(tipo.int32)
        TotalStamina = data.read(tipo.int32)
        ReRemaining = data.read(tipo.int32)
        TotalRe = data.read(tipo.int32)
        data.skip(8)
        ItemLevelInventory = data.read(tipo.int32)
        ItemLevel = data.read(tipo.int32)


#     def __init__(self, tracker, time, direction, opcode, data):
#         cur_hp = data.read(tipo.int32)
#         cur_mp = data.read(tipo.int32)
#         unk1 = data.read(tipo.int32)
#         max_hp = data.read(tipo.int32)
#         max_mp = data.read(tipo.int32)
#         base_power = data.read(tipo.int32)
#         base_endurance = data.read(tipo.int32)
#         base_impact_factor = data.read(tipo.int32)
#         base_balance_factor = data.read(tipo.int32)
#         base_movement_speed = data.read(tipo.int16)
#         unk2 = data.read(tipo.int16)
#         base_attack_speed = data.read(tipo.int16)
#         base_crit_rate = data.read(tipo.float)
#         base_crit_resist = data.read(tipo.float)
#         base_crit_power = data.read(tipo.float)
#         base_attack = data.read(tipo.int32)
#         base_attack2 = data.read(tipo.int32)
#         base_defense = data.read(tipo.int32)
#         base_impact = data.read(tipo.int32)
#         base_balance = data.read(tipo.int32)
#         base_resist_weakening = data.read(tipo.float)
#         base_resist_periodic = data.read(tipo.float)
#         base_resist_stun = data.read(tipo.float)
#         bonus_power = data.read(tipo.int32)
#         bonus_endurance = data.read(tipo.int32)
#         bonus_impact_factor = data.read(tipo.int32)
#         bonus_balance_factor = data.read(tipo.int32)
#         bonus_movement_speed = data.read(tipo.int16)
#         unk3 = data.read(tipo.int16)
#         bonus_attack_speed = data.read(tipo.int16)
#         bonus_crit_rate = data.read(tipo.float)
#         bonus_crit_resist = data.read(tipo.float)
#         bonus_crit_power = data.read(tipo.float)
#         bonus_attack = data.read(tipo.int32)
#         bonus_attack2 = data.read(tipo.int32)
#         bonus_defense = data.read(tipo.int32)
#         bonus_impact = data.read(tipo.int32)
#         bonus_balance = data.read(tipo.int32)
#         bonus_resist_weakening = data.read(tipo.float)
#         bonus_resist_periodic = data.read(tipo.float)
#         bonus_resist_stun = data.read(tipo.float)
#         level = data.read(tipo.int32)
#         vitality = data.read(tipo.int16)
#         status = data.read(tipo.byte)
#         bonus_hp = data.read(tipo.int32)
#         bonus_mp = data.read(tipo.int32)
#         cur_stamina = data.read(tipo.int32)
#         max_stamina = data.read(tipo.int32)
#         cur_re = data.read(tipo.int32)
#         max_re = data.read(tipo.int32)
#         unk5 = data.read(tipo.int32)
#         unk6 = data.read(tipo.int32)
#         item_level_inventory = data.read(tipo.int32)
#         item_level = data.read(tipo.int32)
#         unk7 = data.read(tipo.int32)
#         unk8 = data.read(tipo.int32)
#         unk9 = data.read(tipo.int32) # 0x1F40 = 8000
#         unk10 = data.read(tipo.int32) # 3
#         unk11 = data.read(tipo.int32)