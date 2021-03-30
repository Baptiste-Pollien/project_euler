""""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))

from number_tools import convert_int_tab, convert_tab_int

def series_self_power(n):
    """
    Compute the series 1^1 + 2^2 + ... + n^n
    """
    sum_power = 0

    for i in range(1, n + 1):
        sum_power += i**i

    return sum_power

def get_10_digits_self_power(nb, n):
    """
    Get the last nb digits of the series
    1^1 + 2^2 + ... + n^n
    """
    res     = series_self_power(n)
    tab_res = convert_int_tab(res)

    return convert_tab_int(tab_res[-10:])

if __name__ == '__main__':
    res = get_10_digits_self_power(10, 1000)
    print(res)