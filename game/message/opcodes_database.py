class OpcodesDatabase(dict):
    __instance = None

    def __new__(self, *args, **kwargs):  # Singleton
        if not OpcodesDatabase.__instance:
            OpcodesDatabase.__instance = dict.__new__(self, *args, **kwargs)
        return OpcodesDatabase.__instance

    def __init__(self, ver=None):
        self.opcodes_v = None
        if ver: self.read(ver)

    def read(self, ver):
        self.opcodes_v = ver
        with open('data/opcodes/' + ver + '.txt') as f:
            for line in f:
                (val, key) = line.split(" = ")
                try:
                    self[int(key)] = getattr(__import__('game.message.' + val[0] + '.' + val, globals(), locals(), [val], -1), val)
                except Exception as e:
                    # print(val, e)
                    pass
        # print('Parsing opcodes: ', self)
