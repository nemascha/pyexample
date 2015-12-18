# coding=utf-8

import re

s = "A line abcdefgoprstxyz"
m = re.search(r"(?<=cd).*((?<=.op).*(?=y))", s)


print(m.group(0))
print(m.group(1))