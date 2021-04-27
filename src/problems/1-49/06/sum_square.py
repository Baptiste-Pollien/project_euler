"""
The sum of the squares of the first ten natural numbers is,

1²+2²+...+10²=385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025-385=2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

def compute_diff_square_sum(n):
    """
    Compute the difference between the sum of the squares of the first one
    n natural numbers and the square of the sum.
    """
    sum_square = 0
    sum_int    = 0

    for i in range(n + 1):
        sum_square += i*i
        sum_int    += i

    return (sum_int * sum_int - sum_square)

if __name__ == '__main__':
    res = compute_diff_square_sum(100)
    print(res)