"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))

from prime_numbers import Prime_numbers
from number_tools import convert_tab_int, convert_int_tab

# Global variable to compute prime numbers
primes = Prime_numbers()

def is_truncable(el):
    """
    Test if el is a truncable prime number
    """
    l = len(el)

    for i in range(l):
        if not primes.is_prime(convert_tab_int(el[:i+1])) \
            or not primes.is_prime(convert_tab_int(el[i:])):
                return False

    return True

def sum_truncable_prime_numbers():
    """
    Compute the sum of the only eleven primes that are both truncatable 
    from left to right and right to left
    """
    # List of unary prime number
    list_prime        = [2, 3, 5, 7]

    sum_trunc_nb      = 0
    nb_trunc_nb_found = 0

    # Compute the truncable numbers of size 2
    for el in [[i, j] for i in list_prime for j in list_prime]:
        if is_truncable(el):
            sum_trunc_nb += convert_tab_int(el)
            nb_trunc_nb_found += 1

    list_possible = [[3, 7], [7, 3], [3, 3], [7, 7]] 
    list_res      = list(list_possible)

    possible_value = [1, 3, 7, 9] # Possible digit to add
    size           = 2

    #Compute the rest of the truncable number
    while nb_trunc_nb_found < 11:
        new_list=[]

        for value in list_possible:
            for el in possible_value:
                new_value = list(value)
                new_value.insert(1, el)

                if is_truncable(new_value):
                    sum_trunc_nb      += convert_tab_int(new_value)
                    nb_trunc_nb_found += 1

                new_list.append(new_value)

        list_possible = new_list
        size         += 1

    return sum_trunc_nb

if __name__ == '__main__':
    res = sum_truncable_prime_numbers()
    print(res)