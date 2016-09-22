class S_TARGET_INFO(object):

    def __init__(self, time, direction, opcode, reader, version):
        reader.Skip(8)
        Target = reader.ReadEntityId()
