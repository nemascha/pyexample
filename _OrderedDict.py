


import collections

l = list(range(10))
ln = list('' * len(l))

d = collections.OrderedDict(zip(l, ln))

print(l)