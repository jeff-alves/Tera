from util.tipo import tipo
class S_WHISPER(object):

    def __init__(self, tracker, time, direction, opcode, data):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        author_offset = data.read(tipo.offset)
        recipient_offset = data.read(tipo.offset)
        message_offset = data.read(tipo.offset)
        player = data.read(tipo.uint64)
        unk1 = data.read(tipo.byte)
        gm = data.read(tipo.byte)
        unk2 = data.read(tipo.byte)
        author = data.read(tipo.string)
        recipient = data.read(tipo.string)
        message = data.read(tipo.string)
