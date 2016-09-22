class S_GET_USER_LIST(object):

    def __init__(self, time, direction, opcode, reader, version):
        count = reader.ReadUInt16()
        offset = reader.ReadUInt16()
        PlayerGuilds = {}
        for i in xrange(1, count + 1):
            pointer = reader.ReadUInt16()
            nextOffset = reader.ReadUInt16()
            reader.Skip(16)
            playerId = reader.ReadUInt32()
            reader.Skip(286)
            guildId = reader.ReadUInt32()
            PlayerGuilds[playerId] = guildId
            offset = nextOffset
