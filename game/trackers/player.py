
class Player(object):
    __instance = None

    def __new__(self, *args, **kwargs):  # Singleton
        if not Player.__instance:
            Player.__instance = object.__new__(self, *args, **kwargs)
        return Player.__instance

    def __init__(self):
        self.position = None
        self.angle = None
        self.speed = None

    def event_pos(self, pos1, pos2, angle, speed):
        self.position = pos2
        self.angle = angle
        self.speed = speed

        print("Event (Player_pos): ", self.position, self.angle, self.speed)
