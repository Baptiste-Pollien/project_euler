"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d_2d_3d_4=406 is divisible by 2
    d_3d_4d_5=063 is divisible by 3
    d_4d_5d_6=635 is divisible by 5
    d_5d_6d_7=357 is divisible by 7
    d_6d_7d_8=572 is divisible by 11
    d_7d_8d_9=728 is divisible by 13
    d_8d_9d_10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))

from number_tools import convert_tab_int, convert_int_tab, gen_comb_pandigital

def test_property(tab):
    """
    Return True if the property of the problem is verified
    """
    tab_div=[2, 3, 5, 7, 11, 13, 17]

    for i in range(1, 8):
        if (convert_tab_int(tab[i:(i+3)]) % tab_div[i-1] != 0):
            return False

    return True


def sum_pandigital_property():
    """
    Return the sum of pandigital numbers that satisfy
    the property
    """
    # Pre-compute the list of pandigital number
    list_pan = gen_comb_pandigital(9, 0)
    sum_pan  = 0

    for tab in list_pan:
        if test_property(tab):
            sum_pan += convert_tab_int(tab)

    return sum_pan

if __name__ == '__main__':
    res = sum_pandigital_property()
    print(res)