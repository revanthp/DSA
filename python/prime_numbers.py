"""
Find prime numbers upto given number.
"""

from math import sqrt, floor
import time


def get_prime_numbers(max_num):

    prime_numbers = [2]

    for x in range(3, max_num, 2):

        # Start with the hypothesis that everything is a prime number.
        # and try disproving it.
        prime_ = True

        max_div = floor(sqrt(x))

        # try to prove x is not prime.
        for p in prime_numbers:
            if x % p == 0:
                prime_ = False
                break
            if p > max_div:
                break

        if prime_:
            prime_numbers.append(x)

    return prime_numbers


def is_prime(x):

    if x > 2 and x % 2 == 0:
        return False

    if x == 2:
        return False

    if x < 2:
        return False

    for i in range(3, floor(sqrt(x)), 2):
        if x % i == 0:
            return False

    return True


t0 = time.time()
temp = get_prime_numbers(100000)  # count = 9592
t1 = time.time()

print(is_prime(10691))
