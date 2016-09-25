from util import tipo
class S_TRADE_BROKER_DEAL_SUGGESTED(object):

    def __init__(self, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3], len(data), data.get_array_int(1))
        Unknown = data.read(tipo.int64)
        data.skip(14)
        SellerPrice = data.read(tipo.int64)
        OfferedPrice = data.read(tipo.int64)
        PlayerName = data.read(tipo.string)

    def gold(self, price):
        return str(price)[0:-4]

    def silver(self, price):
        return str(price)[-4:-2]

    def bronze(self, price):
        return str(price)[-2:]
