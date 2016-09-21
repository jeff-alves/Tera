class CryptorKey(object):
        def __init__(self, size, max_pos):
            self.size = size
            self.max_pos = max_pos
            self.buffer = [0] * (size * 4)
            self.key = 0
            self.pos1 = 0
            self.pos2 = max_pos
            self.sum = 0
