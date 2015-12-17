# coding=utf-8

import os

a = os.path.split(__file__)
print(a)
print(a[0])
print(a[1])

c = os.path.join(a[0], a[1])
c = os.path.normpath(c)
print(c)

path_to_this_file = os.path.dirname(__file__)
print(path_to_this_file)

file_name = os.path.basename(__file__)
print(file_name)

b = os.path.getsize(__file__)
print('File size is {} B'.format(b))

z = os.path.isfile(__file__)
y = os.path.isdir(__file__)
print(z, y)