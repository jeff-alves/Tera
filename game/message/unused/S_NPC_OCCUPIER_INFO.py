from util.tipo import tipo
class S_NPC_OCCUPIER_INFO(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        id = data.read(tipo.uint64)
        enraged = data.read(tipo.uint64)
        target = data.read(tipo.uint64)
