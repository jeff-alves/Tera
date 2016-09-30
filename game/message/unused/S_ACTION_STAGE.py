from util.tipo import tipo
class S_ACTION_STAGE(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        effects_count = data.read(tipo.count)
        effects_offset = data.read(tipo.offset)
        source = data.read(tipo.uint64)
        pos = data.read(tipo.float, 3)
        angle = data.read(tipo.angle)*360./0x10000
        model = data.read(tipo.uint32)
        skill = data.read(tipo.uint32)  # & 0x3FFFFFF
        stage = data.read(tipo.uint32)
        speed = data.read(tipo.float)
        id = data.read(tipo.uint32)
        unk = data.read(tipo.float)
