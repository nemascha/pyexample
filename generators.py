# coding=utf-8


print(all([1, 1, 0, 1]))
print(any([0, 0, 0, 1]))


#
# Lazy Evaluation
#
q = zip(['a', 'b', 'c'], [1, 2, 3], ('qwe', 'asd', 'zxc'))
print(q)
q = dict(zip(('a', 'b', 'c'), (1, 2, 3)))
print(q)


def generator():
    for i in (1, 2, 3, 4, 5, 6, 7):
        yield i

g = generator()
print(g)
f = next(g)
h = next(g)
a = list(g)
b = a[:]
c = a
a.pop()
print(f)
print(h)
print(a)
print(b)
print(c)
