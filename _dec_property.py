# coding=utf-8


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        assert age >= 0
        self._age = age


if __name__ == '__main__':
    p = Person('Bob', 23)
    print(p.name)
    print(p.age)
    print(p._age)
    p.age = 57
    print(p.age)
    print(p._age)
    p._age = 98
    print(p.age)
    print(p._age)