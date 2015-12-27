# coding=utf-8

'''
def transact(method):
    def transacted_call(slf, *args, **kwargs):
        try:
            transaction = self.start_transaction()
            r = method(slf, *args, **kwargs)
            transaction.commit()
            return r
        except:
            transaction.rollback()
            raise
    return transacted_call

class C:
    @transact
    def update(self, what):
        return
'''

#
# def decorator
#
'''
def decorator(input_function):
    def wrapper():
        print('_________________')
        input_function()
        print('_________________')
    return wrapper

@decorator
@decorator
def a_stand_alone_function():
    print('simpliest function')
#a_stand_alone_function = decorator(a_stand_alone_function)

a_stand_alone_function()
'''

#
# a decorator passing arbitrary arguments
#
'''
def deco(function_to_decorate):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        function_to_decorate(*args, **kwargs)
    return wrapper

class Mary(object):

    def __init__(self):
        self.age = 32

    @deco
    def sayYourAge(self, lie=-3):
        print("I'm {} years.".format(self.age + lie))

m = Mary()
m.sayYourAge()
'''


#
# benchmark
#
'''
import datetime


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        finish = datetime.datetime.now()
        total_seconds = (finish - start).total_seconds()
        print(total_seconds)
    return wrapper

@benchmark
def s():
    out = 6 ** 80
    return out
s()
'''


#
# counter
#

def counter(func):

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(func.__name__, wrapper.count)
    wrapper.count = 0
    return wrapper

@counter
def health():
    print('-')

health()
health()
health()
health()




#
# decorator with args
#
'''
def decorator_with_args(decorator_to_enhance):
    def decorator_maker(*args, **kwargs):
        def dec_wrapper(func):
            return decorator_to_enhance(func, *args, **kwargs)
        return dec_wrapper
    return decorator_maker

@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    def wrapper(fun_arg1, fun_arg2):
        print('I have', args, kwargs)
        return func(fun_arg1, fun_arg2)
    return wrapper

@decorated_decorator
def decorated_function(fun_arg1, fun_arg2):
    print(fun_arg1, fun_arg2)

decorated_function('dg', 'hyy')
'''