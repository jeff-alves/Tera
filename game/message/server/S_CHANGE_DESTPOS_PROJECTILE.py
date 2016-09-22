class S_CHANGE_DESTPOS_PROJECTILE(object):

    def __init__(self, time, direction, opcode, reader, version):
        Id = reader.ReadEntityId()
        Finish = reader.ReadVector3f()
