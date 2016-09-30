from util.tipo import tipo
class S_NPC_LOCATION(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        target = data.read(tipo.uint64)
        pos1 = data.read(tipo.float, 3)
        angle = data.read(tipo.angle)*360./0x10000
        speed = data.read(tipo.int16)
        pos2 = data.read(tipo.float, 3)
        typ = data.read(tipo.int32)  # 0 = Move, 7= Rotate standing