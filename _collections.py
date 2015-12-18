# coding=utf-8

import collections

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 3]
a1 = collections.Counter(l1).most_common(5)
print(a1)

c = collections.Counter()
c['a'] = 2
print(c)
print(c['b']) # if not in the list - returns 0
del c['a']
print(c)

c = collections.Counter(a=4, b=2, c=0, d=-2)
print(list(c.elements()))

'''
# Find the ten most common words in Hamlet
import re
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
Counter(words).most_common(10)
'''

#
#collections.defaultdict
#
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = collections.defaultdict(list) # or list => set
print(d)
for k, v in s:
    #print(k, v, d[k])
    d[k].append(v)
print(d.items())


s = 'mississippi'
d = collections.defaultdict(int)
for k in s:
    d[k] += 1
print(d.items())


# regular unsorted dictionary
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}

# dictionary sorted by key
d1 = collections.OrderedDict(sorted(d.items(), key=lambda t: t[0]))

# dictionary sorted by value
d2 = collections.OrderedDict(sorted(d.items(), key=lambda t: t[1]))

# dictionary sorted by length of the key string
d3 = collections.OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))

print(d1)
print(d2)
print(d3)