class S_NPC_STATUS(object):

    def __init__(self, time, direction, opcode, reader, version):
        Npc = reader.ReadEntityId()
        Enraged = (reader.ReadByte() & 1) == 1
        reader.Skip(4)
        Target = reader.ReadEntityId()
