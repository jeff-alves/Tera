from util.tipo import tipo
class S_ABNORMALITY_BEGIN(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        target = data.read(tipo.uint64)
        source = data.read(tipo.uint64)
        abnormality_id = data.read(tipo.int32)
        duration = data.read(tipo.int32)
        stacks = data.read(tipo.int32)

        tracker.abnormality.add(target, source, abnormality_id, duration, stacks)
