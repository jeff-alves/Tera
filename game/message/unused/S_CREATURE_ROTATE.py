from util.tipo import tipo
class S_CREATURE_ROTATE(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        id = data.read(tipo.uint64)
        angle = data.read(tipo.angle)*360./0x10000
        delay = data.read(tipo.int16)
