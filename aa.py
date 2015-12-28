# coding=utf-8

class A: pass
class B(A): pass
a = A()
b = B()
print(type(a))
print(type(b))

class C(object): pass
class D(C): pass
c = C()
d = D()

print(type(c))
print(type(d))