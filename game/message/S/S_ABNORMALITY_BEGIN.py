from util.tipo import tipo
class S_ABNORMALITY_BEGIN(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        dic = {}
        dic['target'] = data.read(tipo.uint64)
        dic['source'] = data.read(tipo.uint64)
        dic['abnormality_id'] = data.read(tipo.int32)
        dic['duration'] = data.read(tipo.int32)
        dic['stacks'] = data.read(tipo.int32)

        tracker.abnormality.add(dic)
