"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the
factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))

from number_tools import convert_int_tab, gen_comb_pandigital
from functools import reduce


# Global variable containing the result of the factorial
# for all digits
tab_fact = [1]

for i in range(9):
    tab_fact.append(tab_fact[i] * (i+1))

def compute_sum_fact(nb, m):
    """ 
    Compute the sum of the fact of all digit of nb
    return -1 is in nb use digit > m or sum > m
    """
    sum_fact = 0

    for i in convert_int_tab(nb):
        if i > m:
            return -1

        sum_fact += tab_fact[i]

    return sum_fact

def sum_factorial_digit():
    """
    Compute the sum of all numbers which are equal to the sum of the
    factorial of their digits
    """
    # The number can not have more than 7 digits

    # Tab where index is the number of digit used
    # and the value is the max digit that can be used
    max_digits = [0, 0, 4, 6, 7, 8, 9, 9]

    sum_nb     = 0
    for nb_digits in range(2, 8):
        m      = max_digits[nb_digits]
        max_nb = 10**nb_digits
        min_nb = 10**(nb_digits-1)

        for nb in range(min_nb, max_nb):
            if compute_sum_fact(nb, m) == nb:
                sum_nb += nb

    return sum_nb

if __name__ == '__main__':
    res = sum_factorial_digit()
    print(res)