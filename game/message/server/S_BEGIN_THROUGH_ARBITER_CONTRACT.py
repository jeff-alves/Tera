from util import tipo

class S_BEGIN_THROUGH_ARBITER_CONTRACT(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        data.skip(18)
        InviteName = data.read(tipo.string)
        PlayerName = data.read(tipo.string)
