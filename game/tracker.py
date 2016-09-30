from game.trackers.abnormality import Abnormality
from game.trackers.party import Party
from game.trackers.player import Player


class Tracker(object):
    __instance = None

    def __new__(self, *args, **kwargs):  # Singleton
        if not Tracker.__instance:
            Tracker.__instance = object.__new__(self, *args, **kwargs)
        return Tracker.__instance

    def __init__(self):
        self.player = Player(self)
        self.party = Party(self)
        self.abnormality = Abnormality(self)
