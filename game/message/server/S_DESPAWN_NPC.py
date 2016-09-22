class S_DESPAWN_NPC(object):

    def __init__(self, time, direction, opcode, reader, version):
        Npc = reader.ReadEntityId()
        Position = reader.ReadVector3f()
        Dead = reader.ReadByte() == 5  # 1 = move out of view, 5 = death
