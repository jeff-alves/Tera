class S_REQUEST_CONTRACT(object):

    def __init__(self, time, direction, opcode, reader, version):
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

        reader.Skip(24)
        Type = RequestType[reader.ReadInt16()]
        reader.Skip(14)
        # unk3 = reader.ReadInt32()
        # time = reader.ReadInt32()
        Sender = reader.ReadTeraString()
        Recipient = reader.ReadTeraString()
