class S_REMOVE_CHARM_STATUS(object):

    def __init__(self, time, direction, opcode, reader, version):
        CharmId = reader.ReadUInt32()
