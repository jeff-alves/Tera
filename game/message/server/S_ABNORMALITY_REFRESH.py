class S_ABNORMALITY_REFRESH(object):

    def __init__(self, time, direction, opcode, reader, version):
        TargetId = reader.ReadEntityId()
        AbnormalityId = reader.ReadInt32()
        Duration = reader.ReadInt32()
        Unknow = reader.ReadInt32()
        StackCounter = reader.ReadInt32()
