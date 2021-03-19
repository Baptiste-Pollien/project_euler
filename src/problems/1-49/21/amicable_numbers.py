"""
Let d(n) be defined as the sum of proper divisors of n (numbers less
than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable
pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of
284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt

def d(n):
    """
    Compute the sum of proper divisors of n
    """
    sum_prop_div = 1

    for i in range(2, n):
        if (i * i > n):
            break
        if (n % i == 0):
            sum_prop_div  += n // i + i

    return sum_prop_div 

def is_amicable(n):
    """
    Return true if n is a amicable number
    """
    a = d(n)
    b = d(a)

    return (b == n and a != n)

def sum_all_amicable_number(max_val):
    """
    Compute the sum of all amicable number under max_val
    """
    sum_amicable = 0

    for nb in range(10000):
        if is_amicable(nb):
            sum_amicable += nb

    return sum_amicable

if __name__ == '__main__':
    res = sum_all_amicable_number(10000)
    print(res)