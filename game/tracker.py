from game.trackers.abnormality import Abnormality
from game.trackers.entity import Entity
from game.trackers.party import Party
from util.util import singleton

@singleton
class Tracker(object):

    def __init__(self):
        self.entity = {}  # Entities
        self.player = None
        self.party = Party(self)
        self.abnormality = Abnormality(self)

    def get_entity(self, id):
        e = self.entity.get(id)
        if not e:
            e = Entity(self)
            self.entity[id] = e
        return e

