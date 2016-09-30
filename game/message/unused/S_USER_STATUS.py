from util.tipo import tipo
class S_USER_STATUS(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        target = data.read(tipo.uint64)
        status = data.read(tipo.byte)
