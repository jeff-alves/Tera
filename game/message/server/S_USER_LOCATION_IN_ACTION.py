from util import tipo
class S_USER_LOCATION_IN_ACTION(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
