class S_PARTY_MEMBER_ABNORMAL_REFRESH(object):

    def __init__(self, time, direction, opcode, reader, version):
        ServerId = reader.ReadUInt32()
        PlayerId = reader.ReadUInt32()
        AbnormalityId = reader.ReadInt32()
        Duration = reader.ReadInt32()
        Unknow = reader.ReadInt32()
        StackCounter = reader.ReadInt32()
