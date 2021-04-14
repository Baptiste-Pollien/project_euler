"""
By replacing the 1st digit of the 2-digit number *3, it turns out that 
six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, 
this 5-digit number is the first example having seven primes among 
the ten generated numbers, yielding the family: 56003, 56113, 56333, 
56443, 56663, 56773, and 56993. Consequently 56003, being the first 
member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number 
(not necessarily adjacent digits) with the same digit, is part of an 
eight prime value family.
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))
from functools import reduce

from prime_numbers import Prime_numbers
from number_tools import convert_tab_int, convert_int_tab, is_permutation

primes = Prime_numbers()

def is_family_nember(number, i, j, n):
    """
    Test there are at least n primes number 
    bu replacing the ith and jth digit of number
    with the same digit
    """
    nb_find    = 0
    to_test    = 0
    list_value = []
    tab_number = convert_int_tab(number)

    # Test all digits
    while to_test < 10:
        tab_number[i]  = to_test
        tab_number[j]  = to_test
        number_to_test = convert_tab_int(tab_number)

        if primes.is_prime(number_to_test):
            nb_find += 1
            list_value.append(number_to_test)

            if nb_find == n:
                break

        to_test += 1

    if n <= nb_find:
        return list_value
    else:
        return None

assert([56003, 56113, 56333, 56443, 56663, 56773, 56993] == is_family_nember(56003, 2, 3, 7))
assert(None == is_family_nember(56003, 2, 3, 8))
assert(None == is_family_nember(57000, 2, 3, 7))

def compute_n_prime_familly(n):
    """
    Compute the list of n prime value familly 
    ie all prime numbers where part of the number are replaced by 2
    same digits.
    """
    nb_to_test = 100
    list_res = None

    while list_res is None:
        for i 

assert(56003 in compute_n_prime_familly(7))

if __name__ == '__main__':
    pass
