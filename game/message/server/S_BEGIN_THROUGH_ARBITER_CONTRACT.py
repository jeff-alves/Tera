class S_BEGIN_THROUGH_ARBITER_CONTRACT(object):

    def __init__(self, time, direction, opcode, reader, version):
        reader.Skip(18)
        InviteName = reader.ReadTeraString()
        PlayerName = reader.ReadTeraString()
