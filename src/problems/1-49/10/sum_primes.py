"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))

from prime_numbers import Prime_numbers
from functools import reduce

def find_sum_primes_below_n(n):
    """
    Find the sum of all the primes below
    """
    primes = Prime_numbers()

    primes.compute_prime_number_until(n + 1)

    return reduce(lambda n, y: n + y, primes.primes, 0)

if __name__ == '__main__':
    res = find_sum_primes_below_n(2000000)
    print(res)