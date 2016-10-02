from util.tipo import tipo
class S_ENABLE_CHARM_STATUS(object):

    def __init__(self, tracker, time, direction, opcode, data):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        id = data.read(tipo.uint32)
