# uncoment to use

from game.message.client.C_CHECK_VERSION import C_CHECK_VERSION
from game.message.client.C_PLAYER_LOCATION import C_PLAYER_LOCATION

from game.message.server.S_ABNORMALITY_BEGIN import S_ABNORMALITY_BEGIN
from game.message.server.S_ABNORMALITY_END import S_ABNORMALITY_END
from game.message.server.S_ABNORMALITY_REFRESH import S_ABNORMALITY_REFRESH
from game.message.server.S_ACTION_END import S_ACTION_END
from game.message.server.S_ACTION_STAGE import S_ACTION_STAGE
from game.message.server.S_BAN_PARTY_MEMBER import S_BAN_PARTY_MEMBER
from game.message.server.S_BOSS_GAGE_INFO import S_BOSS_GAGE_INFO
from game.message.server.S_CHANGE_DESTPOS_PROJECTILE import S_CHANGE_DESTPOS_PROJECTILE
from game.message.server.S_CHAT import S_CHAT
from game.message.server.S_CREATURE_CHANGE_HP import S_CREATURE_CHANGE_HP
from game.message.server.S_CREATURE_LIFE import S_CREATURE_LIFE
from game.message.server.S_CREATURE_ROTATE import S_CREATURE_ROTATE
from game.message.server.S_DESPAWN_NPC import S_DESPAWN_NPC
from game.message.server.S_DESPAWN_USER import S_DESPAWN_USER
from game.message.server.S_EACH_SKILL_RESULT import S_EACH_SKILL_RESULT
from game.message.server.S_ENABLE_CHARM_STATUS import S_ENABLE_CHARM_STATUS
from game.message.server.S_GET_USER_GUILD_LOGO import S_GET_USER_GUILD_LOGO
from game.message.server.S_GET_USER_LIST import S_GET_USER_LIST
from game.message.server.S_INSTANT_MOVE import S_INSTANT_MOVE
from game.message.server.S_LEAVE_PARTY_MEMBER import S_LEAVE_PARTY_MEMBER
from game.message.server.S_LOGIN import S_LOGIN
from game.message.server.S_MOUNT_VEHICLE_EX import S_MOUNT_VEHICLE_EX
from game.message.server.S_NPC_LOCATION import S_NPC_LOCATION
from game.message.server.S_NPC_OCCUPIER_INFO import S_NPC_OCCUPIER_INFO
from game.message.server.S_NPC_STATUS import S_NPC_STATUS
from game.message.server.S_NPC_TARGET_USER import S_NPC_TARGET_USER
from game.message.server.S_PARTY_MEMBER_ABNORMAL_ADD import S_PARTY_MEMBER_ABNORMAL_ADD
from game.message.server.S_PARTY_MEMBER_ABNORMAL_DEL import S_PARTY_MEMBER_ABNORMAL_DEL
from game.message.server.S_PARTY_MEMBER_ABNORMAL_REFRESH import S_PARTY_MEMBER_ABNORMAL_REFRESH
from game.message.server.S_PARTY_MEMBER_CHANGE_HP import S_PARTY_MEMBER_CHANGE_HP
from game.message.server.S_PARTY_MEMBER_CHANGE_MP import S_PARTY_MEMBER_CHANGE_MP
from game.message.server.S_PARTY_MEMBER_CHARM_ADD import S_PARTY_MEMBER_CHARM_ADD
from game.message.server.S_PARTY_MEMBER_CHARM_DEL import S_PARTY_MEMBER_CHARM_DEL
from game.message.server.S_PARTY_MEMBER_CHARM_ENABLE import S_PARTY_MEMBER_CHARM_ENABLE
from game.message.server.S_PARTY_MEMBER_CHARM_RESET import S_PARTY_MEMBER_CHARM_RESET
from game.message.server.S_PARTY_MEMBER_LIST import S_PARTY_MEMBER_LIST
from game.message.server.S_PARTY_MEMBER_STAT_UPDATE import S_PARTY_MEMBER_STAT_UPDATE
from game.message.server.S_PLAYER_CHANGE_MP import S_PLAYER_CHANGE_MP
from game.message.server.S_PLAYER_STAT_UPDATE import S_PLAYER_STAT_UPDATE
from game.message.server.S_REMOVE_CHARM_STATUS import S_REMOVE_CHARM_STATUS
from game.message.server.S_RESET_CHARM_STATUS import S_RESET_CHARM_STATUS
from game.message.server.S_SPAWN_ME import S_SPAWN_ME
from game.message.server.S_SPAWN_NPC import S_SPAWN_NPC
from game.message.server.S_SPAWN_PROJECTILE import S_SPAWN_PROJECTILE
from game.message.server.S_SPAWN_USER import S_SPAWN_USER
from game.message.server.S_START_USER_PROJECTILE import S_START_USER_PROJECTILE
from game.message.server.S_TARGET_INFO import S_TARGET_INFO
from game.message.server.S_USER_LOCATION import S_USER_LOCATION
from game.message.server.S_USER_STATUS import S_USER_STATUS
from game.message.server.S_WHISPER import S_WHISPER


def parse_opcodes(file):
    opcodes = {}
    with open('data/opcodes/' + file + '.txt') as f:
        for line in f:
            (val, key) = line.split(" = ")
            try:
                opcodes[int(key)] = eval(val)
            except Exception as e:
                # print(val, e)
                pass
    return opcodes