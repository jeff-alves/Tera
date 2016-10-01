from inspect import stack
from game.trackers.entity import Entity
class Player(Entity):

    def __init__(self, super):
        Entity.__init__(self, super)

    def login(self, dic):
        self.dic.update(dic)
        print('Event(' + self.__class__.__name__ + '.' + stack()[0][3] + '): ', dic)
