"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 
28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called
abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written 
as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers 
greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot 
be reduced any further by analysis even though it is known that the greatest number that cannot be 
expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def is_abundant(n):
    """
    Return True if n is an abundant number 
    """
    sum_div = 1

    for nb in range(2, n):
        if (nb * nb > n):
            break

        if (n % nb == 0):
            sum_div += nb

            if (nb != n // nb):
                sum_div += n // nb

    return sum_div > n

def compute_list_abundant():
    """
    Compute the list of abundant numbers
    """
    list_abundant = []

    for i in range(1, 28124):
        if is_abundant(i):
            list_abundant.append(i)

    return list_abundant

def compute_sum():
    """
    Compute the sum of all the positive integers which cannot be 
    written as the sum of two abundant numbers.
    """
    list_abundant = compute_list_abundant()

    # Compute the set of all interger made from 2 abundant number
    set_sum_2_abundant = set()

    for x in list_abundant:
        for y in list_abundant:
            if (x + y <= 28124):
                set_sum_2_abundant.add(x+y)

    sum_n_abundant = 0

    for nb in range(1, 28124):
        if not (nb in set_sum_2_abundant):
            sum_n_abundant += nb

    return sum_n_abundant


if __name__ == '__main__':
    res = compute_sum()
    print(res)