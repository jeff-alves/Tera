class S_NPC_OCCUPIER_INFO(object):

    def __init__(self, time, direction, opcode, reader, version):
        NPC = reader.ReadEntityId()
        Engager = reader.ReadEntityId()
        Target = reader.ReadEntityId()
