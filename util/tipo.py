class tipo(object):
    bool = ('?', 1)
    char = ('c', 1)
    int8 = ('b', 1)
    uint8 = ('B', 1)
    byte = ('B', 1)
    int16 = ('h', 2)
    uint16 = ('H', 2)
    angle = ('H', 2)
    count = ('H', 2)
    offset = ('H', 2)
    int32 = ('i', 4)
    uint32 = ('I', 4)
    int64 = ('q', 8)
    uint64 = ('Q', 8)
    id = ('Q', 8)
    long32 = ('l', 4)
    ulong32 = ('L', 4)
    longlong64 = ('q', 8)
    ulonglong64 = ('Q', 8)
    float = ('f', 4)
    float32 = ('f', 4)
    double = ('d', 8)
    double64 = ('d', 8)
    string = ('s', 0)
