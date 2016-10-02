from util.tipo import tipo
class S_PARTY_MEMBER_CHANGE_STAMINA(object):

    def __init__(self, tracker, time, direction, opcode, data):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        # target = data.read(tipo.int64)
        # #current_re = data.read(tipo.int32)
        # max_re = data.read(tipo.int32)
        # unk = data.read(tipo.int32)
        pass
