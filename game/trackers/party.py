from inspect import stack
class Party(object):

    def __init__(self, super):
        self.super = super
        self.dic = {}

    def list(self, dic):
        self.dic.update(dic)
        print('Event(' + self.__class__.__name__ + '.' + stack()[0][3] + '): ', dic)
