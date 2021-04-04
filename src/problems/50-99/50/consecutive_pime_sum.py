"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to
a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds
to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the
most consecutive primes?
"""

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))
from functools import reduce

from prime_numbers import Prime_numbers
from number_tools import gen_comb_number, convert_tab_int, convert_int_tab

# Global variable to compute prime numbers
primes = Prime_numbers()


def find_longest_sum_prime(max_value):
    """
    Find the prime below max_value that can be written as the sum of
    the most consecutive primes
    """
    # Compute the maximum sum possible
    list_possible_primes = []
    sum_prime = 0
    nb_poss_prime = 0
    for p_number in primes.it_primes():
        if sum_prime <= max_value:
            list_possible_primes.append(p_number)
            sum_prime     += p_number
            nb_poss_prime += 1
        else:
            break

    # Find the longest sequence
    max_length = -1
    max_prime  = -1

    for start in range(nb_poss_prime):
        if nb_poss_prime - start < max_length:
            break

        sum    = 0
        length = 0

        for i in range(start, nb_poss_prime):
            sum    += list_possible_primes[i]
            length += 1

            if sum > max_value:
                break

            if primes.is_prime(sum) and length > max_length:
                max_length = length
                max_prime = sum

    return max_prime

if __name__ == '__main__':
    res = find_longest_sum_prime(1000000)
    print(res)