"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit
numbers.

"""
from math import sqrt

def gen_palindrome_3():
    """
    Generate all palindrome that can be
    the product of 3-digit numbers.
    From the greatest to the lowest
    """
    for i in range(9, -1, -1):
        extern = i * 100001
        for j in range(9, -1, -1):
            middle = j * 10010
            for k in range(9, -1, -1):
                palindrome = extern + middle + k * 1100
                # 10000  = 100 * 100, with 100 min of 3-digit numbers
                # 998001 = 999 * 999, with 999 max of 3-digit numbers
                if ( 10000 <= palindrome <= 998001):
                    yield palindrome

def largest_palindrome_prod_3_digit_numbers():
    """
    Compute the largest palindrome made from the product of 
    two 3-digit numbers.
    """
    # For all 3-digit palindrome
    for p in gen_palindrome_3():
        # For possible divisors of the palindrome
        for div in range(int(sqrt(float(p)))-1, int(p/100)+1):
            # Verify that it's the product of two 3-digit numbers
            if (999 >= div >= 100 and p % div == 0 and 999 >= p // div >= 100 ):
                return p


if __name__ == '__main__':
    res = largest_palindrome_prod_3_digit_numbers()
    print(res)