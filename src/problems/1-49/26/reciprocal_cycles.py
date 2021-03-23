"""
A unit fraction contains 1 in the numerator. The decimal
representation of the unit fractions with denominators 2 to 10 are
given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It
can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.
"""

def div_remainder_1(remainder, denum):
    """
    The function return quotient, remainder and exp value. 
    quotient corresponds to the exp first fractional digits 
    of the division remainder // denum of the parameters.
    the remainder returned value is the remainder of the division 
    """
    if remainder == 0:
        return 0, 0, 0

    exp = 1
    num = remainder * 10**exp

    while num < denum:
        exp += 1
        num = remainder * 10**exp

    quotient = (num) // denum
    remainder = (num % denum)

    return quotient, remainder, (exp-1)

def find_length_cycle(n):
    """
    Compute the length of the cycle for 1/n
    """
    remainders = []

    quotient, remainder, _ = div_remainder_1(1, n)

    while not(remainder in remainders):
        remainders.append(remainder)
        quotient, remainder, _ = div_remainder_1(remainder, n)

    if remainder == 0:
        return 0
    else:
        cycles = [quotient]
        quotient2, remainder2, nb_zero = div_remainder_1(remainder, n)

        if (quotient2 == quotient and remainder == remainder2):
            for _ in range(nb_zero):
                cycles.append(0)

        while quotient2 != quotient or remainder2 != remainder:
            cycles.append(quotient2)
            for _ in range(nb_zero):
                cycles.append(0)
            quotient2, remainder2, nb_zero = div_remainder_1(remainder2, n)

        return len(cycles)

def find_max_cycles(d_sup):
    """
    Find the value of d < d_sup for which 1/d contains the longest
    recurring cycle in its decimal fraction part
    """
    max_length = 1
    max_d      = 3
    for d in range(2, 1000):
        length = find_length_cycle(d)

        if length > max_length:
            max_length = length
            max_d = d

    return max_d

if __name__ == '__main__':
    res = find_max_cycles(1000)
    print(res)