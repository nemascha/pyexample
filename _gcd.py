# coding=utf-8



def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

if __name__ == '__main__':
    print(gcd(6, 12))
    print(gcd(5, 7))