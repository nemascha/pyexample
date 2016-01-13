# coding=utf-8


class S(object):
    def __init__(self, val):    # Вызываемые экземпляры
        self.val = val
    def __call__(self, arg):
        return self.val + arg

class P(object):
    def __init__(self, val):    # Связанные методы
        self.val = val
    def method(self, arg):
        return self.val + arg

s = S(2)
p = P(3)
a = [s, p.method]

for act in a:
    print(act(5))

print(a[-1](5))                             # Индексы

print([act(5) for act in a])                # Генераторы

print(list(map(lambda act: act(5), a)))     # Отображения