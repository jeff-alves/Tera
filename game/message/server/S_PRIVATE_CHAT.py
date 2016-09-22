class S_PRIVATE_CHAT(object):

    def __init__(self, time, direction, opcode, reader, version):
        reader.Skip(4)  # offsets
        Channel = reader.ReadUInt32()
        AuthorId = reader.ReadUInt64()
        AuthorName = reader.ReadTeraString()
        Text = reader.ReadTeraString()
