from util.enums import Race, Gender, PlayerClass
from util.util import singleton

@singleton
class SkillDatabase(dict):

    def __init__(self, loc=None):
        dict.__init__(self)
        if loc: self.read(loc)

    def read(self, loc):
        with open('data/skills/skills-' + loc + '.tsv') as f:
            for line in f:
                l = line.split('\t')
                self.add(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7])

        with open('data/skills/skills-override-' + loc + '.tsv') as f:
            for line in f:
                l = line.split('\t')
                self.add(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7])

    def add(self, id, race, gender, pclass, name, b, hit, icon):
        id = int(id)
        race = getattr(Race, race) if race else None
        gender = getattr(Gender, gender) if gender else None
        pclass = getattr(PlayerClass, pclass) if pclass else None
        b = (True if b.lower() == 'true' else False) if b != None else None
        tmp = self.pop((id, pclass), None)
        if tmp:
            race = race if race else tmp['race']
            gender = gender if gender else tmp['gender']
            pclass = pclass if pclass else tmp['class']
            name = name if name else tmp['name']
            b = b if b != None else tmp['unknow']
            hit = hit if hit else tmp['hit']
            icon = icon if icon else tmp['icon']

        self[(id, pclass)] = {'race':race, 'gender':gender, 'class':pclass, 'name':name, 'unknow':b, 'hit':hit, 'icon':icon.strip()}
