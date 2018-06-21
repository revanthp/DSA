
from math import sqrt

# Fibonacci series: 0,1,1,2,3,5,8,13,21,...
# Fibonacci series: F(n) = F(n-1) + F(n-2)


def fibonacci(n):
    '''
    O(2^n)
    :param n:
    :return:
    '''
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1) + fibonacci(n-2) # O(n-1) * O(n-2) => O(n^2)


def fibonacci(n):
    '''
    O(n)
    :return:
    '''
    a, b = 0, 1
    while n != 0:
        yield a
        a, b = b, a + b
        n -= 1


def fibonacci(n):
    '''
    O(1)
    :param n:
    :return:
    '''
    return ((1+sqrt(5))**n - (1-sqrt(5))**n) / (2**n * sqrt(5))

# find unique element in a list.


def unique(alist):  # time: O(n), space: O(1)

    unique_elements = []
    for elem in alist:
        if elem not in unique_elements:
            unique_elements.append(elem)

    return unique_elements


def unique(alist):  # time: O(n), space: O(1)?
    return set(alist)


x = [1, 1, 3, 4, 5]

print(unique(x))

dict()