class S_DESPAWN_USER(object):

    def __init__(self, time, direction, opcode, reader, version):
        User = reader.ReadEntityId()
