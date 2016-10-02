from util.tipo import tipo
class S_END_CHANGE_USER_APPEARANCE(object):

    def __init__(self, tracker, time, direction, opcode, data):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        ok = data.read(tipo.byte)
        unk = data.read(tipo.byte)
