# https://www.codewars.com/kata/57be674b93687de78c0001d9/train/python
"""
Задача состоит в том, чтобы найти наибольшее целое число k, при котором 3^k меньше заданного числа N.
В момент, когда условие 3^k < N перестает выполняться, это означает, что 3^k стало больше или равно N.
Таким образом, последнее значение k, для которого 3^k < N, на самом деле равно k - 1.
"""


def largest_power(N):
    k = 0
    while 3 ** k < N:
        k += 1
    return k - 1