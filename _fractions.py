# coding=utf-8


def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     def __init__(self, top, bottom):
         common = gcd(top, bottom)
         self.num = top // common
         self.den = bottom // common

     def getNum(self):
         return self.num

     def getDen(self):
         return self.den

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + self.den*otherfraction.num
         newden = self.den * otherfraction.den
         return Fraction(newnum, newden)

     def __iadd__(self,otherfraction):
         newnum = self.num*otherfraction.den + self.den*otherfraction.num
         newden = self.den * otherfraction.den
         return Fraction(newnum, newden)

     def __sub__(self, otherfraction):
         newnum = self.num*otherfraction.den - self.den*otherfraction.num
         newden = self.den * otherfraction.den
         return Fraction(newnum, newden)

     def __mul__(self, otherfraction):
         newnum = self.num*otherfraction.num
         newden = self.den * otherfraction.den
         return Fraction(newnum, newden)

     def __truediv__(self, otherfraction):
         newnum = self.num * otherfraction.den
         newden = self.den * otherfraction.num
         return Fraction(newnum, newden)

     def __div__(self, otherfraction):
         newnum = self.num * otherfraction.den
         newden = self.den * otherfraction.num
         return Fraction(newnum, newden)

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den


#     def __str__(self):
#         return str(self.num)+"/"+str(self.den)

     def __repr__(self):
         return str(self.num)+"/"+str(self.den)

         return firstnum == secondnum

if __name__ == '__main__':
    a = Fraction(1, 7)
    b = Fraction(3, 7)
