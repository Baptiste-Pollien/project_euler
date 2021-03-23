"""
An irrational decimal fraction is created by concatenating the
positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the
value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

"""

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))

from number_tools import convert_int_tab

def product_decimal(n):
    """
    Compute d_1 * d_10 * ... * d_n
    We suppose than n = 10**x
    """
    current_n = 1 # Current d_(current_n) computed
    nb        = 0 # Current nb in the fractional part
    pos       = 0 # Position in the fractional part
    res       = 1 # result of the product

    while current_n <= n:
        nb += 1

        for i in convert_int_tab(nb):
            pos += 1

            # if i is d_(current_n)
            if pos == current_n:
                res *= i
                current_n *= 10

    return res

if __name__ == '__main__':
    res = product_decimal(1000000)
    print(res)