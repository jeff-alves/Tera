from util.tipo import tipo
class S_NPC_STATUS(object):

    def __init__(self, tracker, time, direction, opcode, data):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        id = data.read(tipo.uint64)
        enraged = data.read(tipo.byte)  # & 1
        unk1 = data.read(tipo.int32)
        target = data.read(tipo.uint64)
        unk2 = data.read(tipo.int32)
