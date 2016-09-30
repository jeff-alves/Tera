from util.tipo import tipo
class S_PRIVATE_CHAT(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        data.skip(4)  # offsets
        Channel = data.read(tipo.uint32)
        AuthorId = data.read(tipo.uint64)
        AuthorName = data.read(tipo.string)
        Text = data.read(tipo.string)
