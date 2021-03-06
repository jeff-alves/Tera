from util.enums import DotType
from util.util import singleton

@singleton
class HotDotDatabase(dict):

    def __init__(self, loc=None):
        dict.__init__(self)
        if loc: self.read(loc)

    def read(self, loc):
        with open('data/hotdot/hotdot-' + loc + '.tsv') as f:
            for line in f:
                l = line.split('\t')
                self.add(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11])

        self.add(8888888, 'Endurance', 0, 0, 0, 0, 0, 0, 'Enrage', '', '', 'enraged')
        self.add(8888889, 'CritPower', 0, 0, 0, 0, 0, 0, 'Slaying', '', "'Slaying' crystal is working (if equipped) when player in this state.", 'slaying')

    def add(self, id, tp, hp, mp, method, time, tick, amount, name, item_name, tooltip, icon_name):
        method = getattr(DotType, method) if method else None
        self[int(id)] = {'tp':tp, 'hp':float(hp), 'mp':float(mp), 'method':method, 'time':int(time), 'tick':int(tick), 'amount':float(amount), 'name':name, 'item_name':item_name, 'tooltip':tooltip, 'icon_name':icon_name.strip()}
