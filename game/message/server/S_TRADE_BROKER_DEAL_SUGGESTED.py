class S_TRADE_BROKER_DEAL_SUGGESTED(object):

    def __init__(self, time, direction, opcode, reader, version):
        Unknown = reader.ReadInt64()
        reader.Skip(14)
        SellerPrice = reader.ReadInt64()
        OfferedPrice = reader.ReadInt64()
        PlayerName = reader.ReadTeraString()

    def gold(self, price):
        return str(price)[0:-4]

    def silver(self, price):
        return str(price)[-4:-2]

    def bronze(self, price):
        return str(price)[-2:]
