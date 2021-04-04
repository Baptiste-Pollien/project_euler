"""
The arithmetic sequence, 1487, 4817, 8147,
in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three
terms are prime, and, (ii) each of the 4-digit
numbers are permutations of one another.

There are no arithmetic sequences made up of 
three 1-, 2-, or 3-digit primes, exhibiting 
this property, but there is one other 
4-digit increasing sequence.

What 12-digit number do you form by 
concatenating the three terms in this sequence?
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))
from functools import reduce

from prime_numbers import Prime_numbers
from number_tools import convert_tab_int, convert_int_tab, is_permutation

# Global variable to compute prime numbers
primes = Prime_numbers()

def find_sequence(n):
    """
    Find sequences of 3 terms which each of the terms 
    increases a delta, and:
    - each of the three terms are prime,
    - each of the n-digit numbers are permutations of one another
    The 3 terms are concatenated
    """
    assert(n >= 1)
    sequences = []

    # Testing all 4 digits number
    for p in primes.it_primes():
        if (p < 10**(n-1)):
            continue

        if (p > 10**n - 1):
            break

        for j in range(p + 1, 10**n - 1):
            if (not primes.is_prime(j)) or (not is_permutation(p, j)):
                continue

            k = j + (j - p)

            if k > 10**n - 1:
                break

            if primes.is_prime(k) and is_permutation(k, j):
                list_res = convert_int_tab(p) \
                            + convert_int_tab(j) \
                                + convert_int_tab(k)

                sequences.append(convert_tab_int(list_res))

    return sequences


if __name__ == '__main__':
    res = find_sequence(4)
    res.remove(148748178147)
    print(res[0])