"""
The arithmetic sequence, 1487, 4817, 8147,
in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three
terms are prime, and, (ii) each of the 4-digit
numbers are permutations of one another.

There are no arithmetic sequences made up of 
three 1-, 2-, or 3-digit primes, exhibiting 
this property, but there is one other 
4-digit increasing sequence.

What 12-digit number do you form by 
concatenating the three terms in this sequence?
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))
from functools import reduce

from prime_numbers import Prime_numbers
from number_tools import gen_comb_number, convert_tab_int, convert_int_tab

# Global variable to compute prime numbers
primes = Prime_numbers()

def diff_prime_combi(number):
    """
    Return dictionnaries where key are difference between numbers
    and values are the list of this numbers.
    The numbers tested are prime one that are a permutation of
    number.
    """
    # Creating a sorted list of prime combinations from number
    combinations       = gen_comb_number(number)
    prime_combinations = filter(lambda nb : primes.is_prime(nb), combinations)
    prime_combinations = [x for x in prime_combinations]
    prime_combinations.sort()
    nb_primes_combi = len(prime_combinations)

    # Dictionnaries where key are difference between numbers
    # and values are the list of this numbers
    tab_diff        = {}

    for i in range(nb_primes_combi - 1):
        for j in range(i + 1, nb_primes_combi):
            diff = prime_combinations[j] - prime_combinations[i]

            if not diff in tab_diff:
                tab_diff[diff] = set()

            tab_diff[diff].add(prime_combinations[i])
            tab_diff[diff].add(prime_combinations[j])

    return tab_diff

def gen_initial_sequence(n):
    """
    Generate the list containing all possibility of 
    n digits combinations without their permutation
    (the digit are ordered)
    """
    assert (n >= 1)
    list_combi = [[i] for i in range(1, 11 - n)]

    for i in range(n - 1):
        new_list_combi = []
        for l in list_combi:
            for d in range(l[i] + 1, 10 - n + (i + 2)):
                new_list = list(l)
                new_list.append(d)
                new_list_combi.append(new_list)

        list_combi = new_list_combi

    # Adding 0
    new_list_combi = []
    for l in list_combi:
        new_list = list(l)
        new_list_combi.append(l)

        new_list = list(l)
        new_list[1] = 0
        new_list_combi.append(l)

        new_list = list(l)
        new_list[2] = 0
        new_list_combi.append(l)

    # Convert the tab of digit to integer
    return reduce(lambda l, y: l + [convert_tab_int(y)], list_combi, [])

def find_sequence(n):
    """
    Find sequence of 3 terms which each of the terms 
    increases a delta, and:
    - each of the three terms are prime,
    - each of the n-digit numbers are permutations of one another
    """
    for init_sequence in gen_initial_sequence(n):
        diff_combi = diff_prime_combi(init_sequence)

        for delta in diff_combi:
            if len(diff_combi[delta]) == 3:
                list_res = [convert_int_tab(nb) for nb in diff_combi[delta]]
                list_res.sort()
                list_res = list_res[0] + list_res[1] + list_res[2]

                print(delta, convert_tab_int(list_res))



if __name__ == '__main__':
    res = find_sequence(4)
    print(res)