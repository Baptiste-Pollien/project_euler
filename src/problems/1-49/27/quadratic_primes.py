"""
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the 
consecutive integer values 0 <= n <= 39. However, when is 
divisible n = 40, 40² + 40 + 41 is divisible by 41, and certainly 
when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula n² -79n + 1601 was discovered, which produces 
80 primes for the consecutive values 0 <= n <= 79. The product of 
the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + a*n + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients,
a and b, for the quadratic expression that produces the maximum 
number of primes for consecutive values of n, starting with n = 0 .
"""

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))

from prime_numbers import Prime_numbers

# Global variable to compute prime numbers
primes = Prime_numbers()

def compute_quadratic(a, b, n):
    """
    Compute the quadratic expression
    """
    return n * n + a * n + b

def nb_prime_divisors(a, b):
    """
    Compute the largest N than for any n < N
    the quadratic expression with a and b is a prime number
    """
    nb = 0

    while (primes.is_prime(compute_quadratic(a, b, nb))):
        nb += 1

    return nb-1

def max_consecutive_quadratic_prime(a_sup, b_sup):
    """
    Find the product of the coefficients,
    a and b, for the quadratic expression that produces the maximum 
    number of primes for consecutive values of n,
    with |a| < a_sup and |b| < b_sup
    """
    max_a  = 0
    max_b  = 0
    max_nb = 0

    for a in range(-a_sup + 1, a_sup):
        for b in range(-b_sup + 1, b_sup):
            nb = nb_prime_divisors(a, b)

            if nb > max_nb:
                max_nb, max_a, max_b = nb, a, b

    return max_a *  max_b

if __name__ == '__main__':
    res = max_consecutive_quadratic_prime(1000, 1000)
    print(res)