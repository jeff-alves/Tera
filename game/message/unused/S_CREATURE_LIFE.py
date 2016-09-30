from util.tipo import tipo
class S_CREATURE_LIFE(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        user = data.read(tipo.uint64)
        pos = data.read(tipo.float, 3)
        dead = data.read(tipo.byte) == 0  # 0=dead1=alive
