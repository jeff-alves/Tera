class S_MOUNT_VEHICLE_EX(object):

    def __init__(self, time, direction, opcode, reader, version):
        Owner = reader.ReadEntityId()
        Id = reader.ReadEntityId()
