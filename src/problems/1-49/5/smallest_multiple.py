"""
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
"""

def is_divisible_prime_20(nb):
    """
    Test if nb is divisible by prime number from 11 to 19
    """
    tab = [11, 13, 17, 19]
    for i in range(4):
        if(nb % tab[i] != 0):
            return False
    return True

def is_divisible_20(nb):
    """ 
    Test if nb is divisible by all number from 1 to 20.
    """
    for i in range(1, 21):
        if(nb % i != 0):
            return False

    return True

def find_number_divisible_20():
    """
    Find the smallest positive number that is evenly divisible by all
    of the numbers from 1 to 20
    """
    # Number divisible by number from 1 to 10
    divisible_10 = 2520
    number       = divisible_10

    while True:
        if is_divisible_prime_20(number):
            if is_divisible_20(number):
                return number

        number += divisible_10

if __name__ == '__main__':
    res = find_number_divisible_20()
    print(res)