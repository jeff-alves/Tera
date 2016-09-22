class S_GET_USER_GUILD_LOGO(object):

    def __init__(self, time, direction, opcode, reader, version):
        offset = reader.ReadUInt16()
        size = reader.ReadUInt16()
        PlayerId = reader.ReadUInt32()
        GuildId = reader.ReadUInt32()

        logo = reader.ReadBytes(size)
        # logo to bitmap
