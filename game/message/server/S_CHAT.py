class S_CHAT(object):

    def __init__(self, time, direction, opcode, reader, version):
        ChannelEnum = {
            2:'Guild',
            27:'General',
            0:'Say',
            9:'Greetings',
            4:'Trading',
            26:'Emotes',
            28:'Alliance',
            3:'Area',
            1:'Group',
            32:'Raid'
        }

        reader.Skip(4)  # offsets
        Channel = ChannelEnum[reader.ReadUInt32()]
        reader.Skip(11)
        Username = reader.ReadTeraString()
        Text = reader.ReadTeraString()
