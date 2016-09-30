from util.tipo import tipo

class S_BEGIN_THROUGH_ARBITER_CONTRACT(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])
        data.skip(18)
        InviteName = data.read(tipo.string)
        PlayerName = data.read(tipo.string)
