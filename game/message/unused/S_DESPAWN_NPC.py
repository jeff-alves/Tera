from util.tipo import tipo
class S_DESPAWN_NPC(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        id = data.read(tipo.uint64)
        pos = data.read(tipo.float, 3)
        dead = data.read(tipo.byte)  # 1 = move out of view, 5 = death
        # typ = data.read(tipo.int32)
        # unk = data.read(tipo.int32)
