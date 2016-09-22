class S_WHISPER(object):

    def __init__(self, time, direction, opcode, reader, version):
        reader.Skip(17)
        Sender = reader.ReadTeraString()
        Receiver = reader.ReadTeraString()
        Text = reader.ReadTeraString()
