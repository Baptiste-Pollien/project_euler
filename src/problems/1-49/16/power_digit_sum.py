"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def sum_digit_2_exp_n(n):
    """
    Compute the sum of the digits of the number 2^n
    """
    value     = 2**n
    sum_digit = 0

    while value != 0:
        sum_digit += value % 10
        value     //=10

    return sum_digit

if __name__ == '__main__':
    res = sum_digit_2_exp_n(1000)
    print(res)