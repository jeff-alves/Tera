from util import tipo
class S_COMBATLOG_COMBAT_ENGAGED_MONSTER_LIST(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
