from inspect import stack
from game.services.skill_database import SkillDatabase
class Entity(object):

    def __init__(self, super):
        self.super = super
        self.dic = {}

    def skill(self, dic):
        skill = SkillDatabase().get((dic['skill_id'], self.dic.get('class')))
        target = self.super.get_entity(dic['target_id'])
        # Calc DPS
        print('Event(' + self.__class__.__name__ + '.' + stack()[0][3] + '): ', self.dic, skill, dic, target.dic)

    def location(self, dic):
        self.dic.update(dic)
        print('Event(' + self.__class__.__name__ + '.' + stack()[0][3] + '): ', self.dic)

    def spaw(self, dic):
        self.dic.update(dic)
        print('Event(' + self.__class__.__name__ + '.' + stack()[0][3] + '): ', self.dic)

    def despawn(self, dic):
        self.dic.update(dic)
        print('Event(' + self.__class__.__name__ + '.' + stack()[0][3] + '): ', self.dic)
        del self

    def status(self, dic):
        self.dic.update(dic)
        print('Event(' + self.__class__.__name__ + '.' + stack()[0][3] + '): ', self.dic)

    def login(self, dic):  # only for me
        self.dic.update(dic)
        print('Event(' + self.__class__.__name__ + '.' + stack()[0][3] + '): ', self.dic)
