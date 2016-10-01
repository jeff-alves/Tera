from util.enums import Race, Gender, PlayerClass
class SkillDatabase(dict):
    __instance = None

    def __new__(self, *args, **kwargs):  # Singleton
        if not SkillDatabase.__instance:
            SkillDatabase.__instance = dict.__new__(self, *args, **kwargs)
        return SkillDatabase.__instance

    def __init__(self, loc=None):
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
            race = race if race else tmp[0]
            gender = gender if gender else tmp[1]
            pclass = pclass if pclass else tmp[2]
            name = name if name else tmp[3]
            b = b if b != None else tmp[4]
            hit = hit if hit else tmp[5]
            icon = icon if icon else tmp[6]

        self[(id, pclass)] = (race, gender, pclass, name, b, hit, icon.strip())
