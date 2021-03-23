"""
The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator
and denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""

def gcd(a,b):
    """
    Compute the gcd of a and b 
    """
    while b != 0:
        r    = a % b
        a, b = b, r

    return a
 

def test_fract(i, j):
    """
    Test if i / j can be simply
    """
    ia, ib = i // 10, i % 10
    ja, jb = j // 10, j % 10
    find = False

    if ia == ja:
        num = ib
        denum = jb
        find = True

    if ia == jb:
        num = ib
        denum = ja
        find = True

    if ib == ja:
        num = ia
        denum = jb
        find = True

    if ib == jb:
        num = ia
        denum = ja
        find = True

    if find and denum != 0 and num/denum == i / j:
        if denum * 10 != j and i *10 != num:
            return True

    return False

def prod_simplified_fract():
    """
    Find the product of the four fractions that can be simply.
    The result is given in its lowest common terms, find the 
    value of the denominator
    """
    prod_num   = 1
    prod_denum = 1
    nb_found   = 0

    for i in range(10, 100):
        for j in range(i + 1, 100):
            if test_fract(i, j):
                prod_num   *= i
                prod_denum *= j
                nb_found   += 1

    assert(nb_found == 4)

    return prod_denum // gcd(prod_num, prod_denum)


if __name__ == '__main__':
    res = prod_simplified_fract()
    print(res)