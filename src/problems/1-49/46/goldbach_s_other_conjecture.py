"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9  = 7 + 2 × 1^2
15 = 7 + 2 × 2^2
21 = 3 + 2 × 3^2
25 = 7 + 2 × 3^2
27 = 19 + 2 × 2^2
33 = 31 + 2 × 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))

from prime_numbers import Prime_numbers
from math import sqrt

# Global var to compute prime number
primes = Prime_numbers()

def odd_compositite_iterator():
    """
    Iterator on all odd composite numbers
    """
    odd = 1

    # For all odd number
    while True:

        # That are not prime
        if not primes.is_prime(odd):
            yield odd

        odd += 2

def is_sum_prime_twice_square(number):
    """
    Return true if number can be written as the 
    sum of a prime and twice a square
    """
    # Find the maximum square possible
    max_square = int((number - 2) / 2 + 1)

    # For all possible candidate
    for i in range(1, max_square + 1):

        # If the remainder is prime
        if primes.is_prime(number - 2 * i * i):
            return True

    return False

def find_smallest_conj_goldbach():
    """
    the smallest odd composite that cannot be written 
    as the sum of a prime and twice a square
    """
    for number in odd_compositite_iterator():
        if not is_sum_prime_twice_square()
            return number


if __name__ == '__main__':
    res = find_smallest_conj_goldbach()
    print(res)