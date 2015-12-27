# coding=utf-8

'''
Module for decorating functions.
It print's total seconds function operating.
'''

import datetime


def benchmark(func):
    '''
    Decorator that prints a speed of function operating.
    '''
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        finish = datetime.datetime.now()
        total_seconds = (finish - start).total_seconds()
        print(total_seconds)
    return wrapper