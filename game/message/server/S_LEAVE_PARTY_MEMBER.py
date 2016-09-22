class S_LEAVE_PARTY_MEMBER(object):

    def __init__(self, time, direction, opcode, reader, version):
        nameoffset = reader.ReadUInt16()
        ServerId = reader.ReadUInt32()
        PlayerId = reader.ReadUInt32()
        Name = reader.ReadTeraString()
