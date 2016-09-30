from util.tipo import tipo
class S_SPAWN_ME(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        target = data.read(tipo.uint64)
        pos = data.read(tipo.float, 3)
        angle = data.read(tipo.angle)*360./0x10000
        dead = (data.read(tipo.byte) & 1) == 0
        unk = data.read(tipo.byte)
