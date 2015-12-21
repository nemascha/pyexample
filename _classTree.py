# coding=utf-8

'''
Выполняет обход дерева наследования
'''

def classtree(cls, indent):
    print('.' * indent + cls.__name__)
    for supercls in cls.__name__:
        classtree(supercls, indent + 3)

def instansetree(inst):
    print('Tree os', inst)
    classtree(inst.__class__, 3)

def selftest():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E: pass
    class F(D, E): pass

    instansetree(B())
    instansetree(F())


if __name__ == '__main__':
    selftest()