"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0
+ 0 = 27.

Find the sum of the digits in the number 100!
"""

def fact(n):
    """
    Compute n!
    """
    res = 1

    for i in range(1,n+1):
        res *= i

    return res

def sum_digit_fact(n):
    """
    Compute the sum of the digits in the number n!
    """
    value          = fact(100)
    sum_digit_fact = 0

    while value != 0:
        sum_digit_fact += value % 10
        value //=10

    return sum_digit_fact

if __name__ == '__main__':
    res = sum_digit_fact(100)
    print(res)