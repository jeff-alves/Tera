from util.tipo import tipo
class S_REQUEST_CONTRACT(object):

    def __init__(self, tracker, time, direction, opcode, data, version):
        print(str(type(self)).split('.')[3]+'('+str(len(data))+'): '+ str(data.get_array_hex(1))[1:-1])

        RequestType = {
            15:'DungeonTeleporter',
            8:'Mailbox',
            14:'MapTeleporter',
            53:'TeraClubMapTeleporter',
            54:'TeraClubTravelJournalTeleporter',
            43:'OpenBox',
            52:'LootBox',
            20:'ChooseLootDialog',  # (aka: goldfinger + elion token + ...)
            26:'BankOpen',
            33:'TeraClubDarkanFlameUse',  # or merge multiple item together
            4:'PartyInvite',
            3:'TradeRequest'
        }

        data.skip(24)
        Type = RequestType[data.read(tipo.int16)]
        data.skip(14)
        # unk3 = data.read(tipo.int32)
        # time = data.read(tipo.int32)
        Sender = data.read(tipo.string)
        Recipient = data.read(tipo.string)
