class S_NPC_TARGET_USER(object):

    def __init__(self, time, direction, opcode, reader, version):
        NPC = reader.ReadEntityId()
