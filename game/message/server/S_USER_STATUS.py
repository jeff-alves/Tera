class S_USER_STATUS(object):

    def __init__(self, time, direction, opcode, reader, version):
        User = reader.ReadEntityId()
        Status = reader.ReadByte()
