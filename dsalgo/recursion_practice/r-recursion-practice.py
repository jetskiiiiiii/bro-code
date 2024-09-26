from typing import *

"""
https://www.freedium.cfd/https://python.plainenglish.io/20-python-recursion-practice-questions-9a04308d456e
"""


def factorial(n: int) -> int:
    """
    Write a recursive function factorial(n)
    that takes in a positive integer n,
    and returns the factorial of n (1 x 2 x 3 x … x n)
    """
    # print(n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def summation(n: int) -> int:
    """
    Write a recursive function summation(n)
    that takes in a positive integer n,
    and returns the sum of numbers from 1 to n.
    """
    if n == 1:
        return n
    else:
        return n + summation(n - 1)


def sum_odd(lis: List[int]) -> int:
    """
    Write a recursive function sum_odd(list)
    that takes in a list of integers,
    and returns the sum of only odd numbers inside the list.
    """
    if len(lis) == 1:
        return lis[0]
    for i in range(len(lis)):
        if lis[i] % 2 == 1:
            return lis[i] + sum_odd(lis[i + 1 :])


print(factorial(3))
print(summation(4))
print(sum_odd([1, 2, 3, 4]))  # should print 4
