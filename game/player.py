
class Player(object):
    __instance = None

    def __new__(self, *args, **kwargs):  # Singleton
        if not Player.__instance:
            Player.__instance = object.__new__(self, *args, **kwargs)
        return Player.__instance

    def __init__(self):
        self.position = None
        self.heading = None
        self.speed = None
