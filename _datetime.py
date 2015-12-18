# coding=utf-8

import datetime

s = '2008-12-23 1:2:3:4'
fmt = '%Y-%m-%d %H:%M:%S:%f'

t = datetime.datetime.strptime(s, fmt)
print(t.year)
print(t.month)
print(t.day)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)


