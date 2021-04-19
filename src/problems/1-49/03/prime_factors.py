"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))

from prime_numbers import Prime_numbers

def compute_largest_prime_factor(number):
    """
    Compute the largest prime factor of the number
    """
    primes = Prime_numbers()

    # Current largest prime factor
    largest_pf = -1


    for i in range(2, number+1):
        if primes.is_prime(i):

            # Test if i is a divisor of number
            if (number % i == 0):
                largest_pf = i
                number     = number // i

                if number == 1:
                    break

    return largest_pf

if __name__ == '__main__':
    res = compute_largest_prime_factor(600851475143)
    print(res)