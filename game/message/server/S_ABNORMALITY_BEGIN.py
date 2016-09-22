class S_ABNORMALITY_BEGIN(object):

    def __init__(self, time, direction, opcode, reader, version):
        TargetId = reader.ReadEntityId()
        SourceId = reader.ReadEntityId()
        AbnormalityId = reader.ReadInt32()
        Duration = reader.ReadInt32()
        Stack = reader.ReadInt32()
