from inspect import stack
class Abnormality(object):

    def __init__(self, super):
        self.super = super
        self.dic = {}

    def add(self, dic):
        self.dic.update(dic)
        print('Event(' + self.__class__.__name__ + '.' + stack()[0][3] + '): ', dic)
