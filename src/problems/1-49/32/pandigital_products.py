"""
We shall say that an n-digit number is pandigital if it makes use of
all the digits 1 to n exactly once; for example, the 5-digit number,
15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9
pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure
to only include it once in your sum.
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))

from number_tools import convert_tab_int, gen_comb_pandigital
from functools import reduce


def test_product(a, b, c, set_combi):
    """
    Test the product a * b = c
    If it verified, c is added in the combination set
    """
    if (a * b == c):
        set_combi.add(c)

def test_combi(combi, set_combi):
    """
    Test the all the possibility of a, b and c numbers 
    in combi tab. 
    When a combination is valid, c is added in the set
    set_combi
    """
    for i in range(1, 8):
        for j in range(1, 9-i):
            a = convert_tab_int(combi[0:i])
            b = convert_tab_int(combi[i:i+j])
            c = convert_tab_int(combi[i+j:])

            test_product(a, b, c, set_combi)

def sum_pandigital_product():
    """
    Compute the sum of all products whose multiplicand/multiplier/product
    identity that can be written as a 1 through 9 pandigital
    """
    set_combi_possible = set()

    for combi in gen_comb_pandigital(9):
        test_combi(combi, set_combi_possible)

    return reduce(lambda n, y: n + y, set_combi_possible, 0)

if __name__ == '__main__':
    res = sum_pandigital_product()
    print(res)