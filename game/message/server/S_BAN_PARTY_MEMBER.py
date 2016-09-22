class S_BAN_PARTY_MEMBER(object):

    def __init__(self, time, direction, opcode, reader, version):
        nameoffset = reader.ReadUInt16()
        ServerId = reader.ReadUInt32()
        PlayerId = reader.ReadUInt32()
        reader.Skip(4)  # unknown ffffffff
        Name = reader.ReadTeraString()

