# coding=utf-8


def fib1(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)


fib2 = lambda n: fib2(n - 1) + fib2(n - 2) if n > 2 else 1


def fib3(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a



#
# FIB линейное время выполнение:
#
def pow(x, n, I, mult):
    """
    Возвращает x в степени n. Предполагает, что I – это единичная матрица, которая
    перемножается с mult, а n – положительное целое
    """
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = pow(x, n // 2, I, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(x, y)
        return y
def identity_matrix(n):
    """Возвращает единичную матрицу n на n"""
    r = list(range(n))
    return [[1 if i == j else 0 for i in r] for j in r]
def matrix_multiply(A, B):
    BT = list(zip(*B))
    return [[sum(a * b
                 for a, b in zip(row_a, col_b))
            for col_b in BT]
            for row_a in A]
def fib4(n):
    F = pow([[1, 1], [1, 0]], n, identity_matrix(2), matrix_multiply)
    return F[0][1]


if __name__ == '__main__':
    n = 4
    print('DEBUG: fib1: {}'.format(fib1(n)))
    print('DEBUG: fib2: {}'.format(fib2(n)))
    print('DEBUG: fib3: {}'.format(fib3(n)))
    print('DEBUG: fib4: {}'.format(fib4(n)))