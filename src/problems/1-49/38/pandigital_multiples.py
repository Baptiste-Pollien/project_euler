"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, 
and 5, giving the pandigital, 918273645, which is the concatenated product 
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed 
as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))

from number_tools import convert_tab_int, convert_int_tab, gen_comb_pandigital

def compute_concatenated_product(nb, n):
    """
    Compute the concatenated product of nb and (1, ..., n).
    n > 1
    """
    sum = []
    for i in range(1, n+1):
        sum += convert_int_tab(i*nb)
    return sum


def gen_all_combinaison_number(n):
    """
    Generate all combinaison of number of n digit
    """
    assert(n >= 1)

    all_combi = [[i] for i in range(1, 10)]

    for _ in range(n-1):
        new_combi = []

        for combi in all_combi:
            for nb in range(10):
                tmp = list(combi)
                tmp.append(nb)
                new_combi.append(tmp)

        all_combi = new_combi

    return all_combi

def largest_concatenated_pandigital():
    """
    Compute the largest 1 to 9 pandigital 9-digit number that can be formed 
    as the concatenated product of an integer with (1,2, ... , n)
    """
    all_comb_pandigital = gen_comb_pandigital(9)
    # The maximal value of n for each size of numbers
    max_n               = [10, 6, 4, 4]

    max_conc            = 0

    for nb_size in range(1, 5):
        all_combi = gen_all_combinaison_number(nb_size)

        for n in range(2, max_n[nb_size-1]):
            for value in all_combi:
                val_int = convert_tab_int(value)
                conc_prod = compute_concatenated_product(val_int, n)

                if (conc_prod in all_comb_pandigital):
                    conc_prod_int = convert_tab_int(conc_prod)
                    max_conc = max(max_conc, conc_prod_int)

    return max_conc

if __name__ == '__main__':
    res = largest_concatenated_pandigital()
    print(res)
