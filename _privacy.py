# coding=utf-8


class PrivateExc(Exception): pass

class Privacy:
    def __setattr__(self, key, value):
        if key in self.privates:
            raise PrivateExc(key, self)
        else:
            self.__dict__[key] = value

    def __getattr__(self, key):
        if key in self.privates:
            raise PrivateExc(key, self)
        else:
            return self.__dict__[key]


if __name__ == '__main__':
    class Test1(Privacy):
        privates = ['age']

    class Test2(Privacy):
        privates = ['name', 'pay']
        def __init__(self):
            self.__dict__['name'] = 'Tom'

    x = Test1()
    y = Test2()

    x.name = 'David'
    #y.name = 'John'   # ERROR

    #x.age = 30     # ERROR
    y.age = 50
