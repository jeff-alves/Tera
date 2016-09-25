from util import tipo
class S_PARTY_MEMBER_CHANGE_STAMINA(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        # target = data.read(tipo.int64)
        # #current_re = data.read(tipo.int32)
        # max_re = data.read(tipo.int32)
        # unk = data.read(tipo.int32)
        pass
