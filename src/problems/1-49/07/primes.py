"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))

from prime_numbers import Prime_numbers

def find_n_th_primes(n):
    """
    Find the n th prime number
    """
    primes    = Prime_numbers()
    nb_primes = len(primes.primes)

    for _ in range(nb_primes, n):
        primes.next()

    return primes.get_max_computed_primes()

if __name__ == '__main__':
    res = find_n_th_primes(10001)
    print(res)