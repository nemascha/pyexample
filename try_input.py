# coding=utf-8

def try_input():
    try:
        a = input('Enter a:\n')
        if a < 0:
            raise RuntimeError()
    except RuntimeError:
        print('Only numbers bellow zero permitted.')
        a = try_input()
    return a
print(try_input())
