"""
We shall say that an n-digit number is pandigital if it makes use of
all the digits 1 to n exactly once. For example, 2143 is a 4-digit
pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))

from number_tools import convert_tab_int, gen_comb_pandigital
from prime_numbers import Prime_numbers


def max_prime_pandigital_number():
    """
    Compute the largest n-digit pandigital prime that exists
    """
    primes         = Prime_numbers()
    max_pandigital = 0

    # For all the size of pandigital numbers possible
    for size in range(1, 10):
        for el in gen_comb_pandigital(size):

            # Skip when the first digit show that the number is divisible
            if el[-1] in {2, 4, 5, 6, 8}:
                next

            value = convert_tab_int(el)

            if primes.is_prime(value):
                if value > max_pandigital:
                    max_pandigital = value

    return max_pandigital

if __name__ == '__main__':
    res = max_prime_pandigital_number()
    print(res)