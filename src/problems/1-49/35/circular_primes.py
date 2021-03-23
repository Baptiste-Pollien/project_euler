"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))

from prime_numbers import Prime_numbers

# Global variable to compute prime numbers
primes = Prime_numbers()

def generate_all_rotation(nb):
    """
    Generate the list of all rotation of nb
    """
    list_rotation = [nb]

    max_exp       = 1

    while nb >= max_exp * 10:
        max_exp *= 10

    new_nb = nb // 10 + max_exp * (nb % 10)

    while new_nb != nb:
        list_rotation.append(new_nb)
        new_nb = new_nb // 10 + max_exp * (new_nb % 10)

    return list_rotation

# Global variable containing the set of all circular prime number
list_circular = set()

def is_circular_prime(nb):
    """
    Test if nb is a circular primer number
    """
    if nb in list_circular:
        return True

    if not primes.is_prime(nb):
        return False

    circular = True
    list_rotation = generate_all_rotation(nb)

    for i in list_rotation:
        circular = circular and primes.is_prime(i)

    if circular:
        list_circular.update(list_rotation)

    return circular


def nb_circular_prime_under(n):
    """
    Compute the number of circular prime number under n
    """
    assert(n >= 3)

    nb_circular = 1

    for nb in range(3, n, 2):
        if is_circular_prime(nb):
            nb_circular += 1

    return nb_circular


if __name__ == '__main__':
    res = nb_circular_prime_under(1000000)
    print(res)