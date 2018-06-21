# find factorial of a number

import time


def factorial1(x):
    if x == 1:
        return 1

    return x * factorial1(x - 1)


def factorial3(x):

    out = 1
    for num in range(x):
        out *= num

    return out


print(factorial1(7))  # 5040.