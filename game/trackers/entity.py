from inspect import stack
class Entity(object):

    def __init__(self, super):
        self.super = super
        self.dic = {}

    def pos(self, dic):
        self.dic.update(dic)
        print('Event(' + self.__class__.__name__ + '.' + stack()[0][3] + '): ', dic)