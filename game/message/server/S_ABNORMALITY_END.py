class S_ABNORMALITY_END(object):

    def __init__(self, time, direction, opcode, reader, version):
        TargetId = reader.ReadEntityId()
        AbnormalityId = reader.ReadInt32()
