
class AbnormalDatabase(dict):
    __instance = None

    def __new__(self, *args, **kwargs):  # Singleton
        if not AbnormalDatabase.__instance:
            AbnormalDatabase.__instance = dict.__new__(self, *args, **kwargs)
        return AbnormalDatabase.__instance

    def __init__(self):
        with open('data/hotdot/abnormal.tsv') as f:
            for line in f:
                l = line.split('\t')
                self.add(l[0], l[1])

    def add(self, id, icon):
        self[int(id)] = (icon.strip())
