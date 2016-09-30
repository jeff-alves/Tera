
class AbnormalDatabase(dict):
    def __init__(self):
        dict.__init__(self)
        with open('data/hotdot/abnormal.tsv') as f:
            for line in f:
                l = line.split('\t')
                self.add(l[0], l[1])

    def add(self, id, icon):
        self[int(id)] = (icon.strip())
