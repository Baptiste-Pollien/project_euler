"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))
from functools import reduce

from prime_numbers import Prime_numbers

# Global variable to compute prime numbers
primes = Prime_numbers()

def verify_consecutive(number, n):
    """
    Return true if the number has n distinct prime factors.
    """
    set_factors = primes.set_primes_factors(number)

    if len(set_factors) != n:
        return False

    return True

def first_n_distincts_factors(n):
    """
    Find the first n consecutive integers to have n 
    distinct prime factors each.
    Return the first number.
    """
    nb_to_test = 1
    tab_result = []

    for i in range(n - 1):
        tab_result.append(verify_consecutive(nb_to_test + i, n))

    while True:
        tab_result.append(verify_consecutive(nb_to_test + n - 1, n))

        if reduce(lambda n, y: n and y, tab_result, True):
            return nb_to_test

        tab_result = tab_result[1:]
        nb_to_test +=1

if __name__ == '__main__':
    res = first_n_distincts_factors(4)
    print(res)