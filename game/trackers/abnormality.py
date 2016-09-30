class Abnormality(object):

    def __init__(self):
        pass

    def add(self, target, source, abnormality_id, duration, stacks):
        self.target = target
        self.source = source
        self.id = abnormality_id
        self.duration = duration
        self.stacks = stacks

        print("Event (Abnormality_add): ", target, source, abnormality_id, duration, stacks)