"""
Surprisingly there are only three numbers that can be written as the
sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of
fifth powers of their digits.

"""

def sum_fifth_power():
    """
    Compute the sum of all the numbers that can be written as the sum of
    fifth powers of their digits
    """
    p       = 5 # Power 5
    # Tab with the value of digits to the power of 5
    tab     = [i**p for i in range(10)]
    # All the combination of digits
    tab_val = [(i, j, k, l, m, n) for i in range(10) 
                                    for j in range(10) 
                                        for k in range(10) 
                                            for l in range(10) 
                                                for m in range(10) 
                                                    for n in range(10)]
    sum_numbers = 0

    for (i, j, k, l, m, n) in tab_val:
        # Compute the number equivalent to the combination
        nb =  i + 10 * j + 100 * k + 1000 * l + 10000 * m + 100000 * n

        # Compute the result with the sum of the digit to the power of 5
        power = i**p + j**p + k**p + l**p + m**p + n**p

        if (nb - power == 0 and nb != 0 and nb != 1):
            sum_numbers += nb

    return sum_numbers

if __name__ == '__main__':
    res = sum_fifth_power()
    print(res)