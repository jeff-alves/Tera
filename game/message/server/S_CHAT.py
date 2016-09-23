from util import tipo
class S_CHAT(object):

    def __init__(self, time, direction, opcode, data, version):
        author_name_offset = data.read(tipo.offset)
        message_offset = data.read(tipo.offset)
        channel = data.read(tipo.uint32)
        author_id = data.read(tipo.uint64)
        unk1 = data.read(tipo.byte)
        gm = data.read(tipo.byte)
        unk2 = data.read(tipo.byte)
        author_name = data.read(tipo.string)
        message = data.read(tipo.string)
