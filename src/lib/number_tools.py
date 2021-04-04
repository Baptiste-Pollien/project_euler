"""
Tool functions to work with numbers : 

- c_tab_int:           Convert a tab of numbers into an integer
- c_int_tab:           Convert an integer to a tab of numbers
- gen_comb_pandigital: Generate all combinations of pandigital 
                       with digits from 1 to n
"""
from functools import reduce

def convert_tab_int(tab):
    """
    Convert a tab of numbers into an integer
    """
    exponent = 1
    number   = 0

    for i in range(len(tab) - 1, -1, -1):
        number   += tab[i] * exponent
        exponent *= 10

    return number

def convert_int_tab(nb):
    """
    Convert an integer to a tab of numbers
    """
    return [int(char) for char in str(nb)]

def gen_comb_pandigital(n, start=1):
    """
    Generate all combinations of pandigital with digits from start to n
    """
    assert (n >= 1)

    all_combi = [[]]

    for i in range(start, n + 1):
        # Creating new combination with i as new digit
        new_combi = []

        # For all previous pandigital numbers
        for combi in all_combi:
            # For all positions
            for pos in range(len(combi) + 1):
                # Create a new pandigital number
                tmp = list(combi)
                tmp.insert(pos, i)
                new_combi.append(tmp)

        all_combi = new_combi

    return all_combi

def gen_comb_number_tab(n):
    """
    Generate all combinations from the digits of n
    The result number are represented as tab of digits
    """
    assert (n >= 1)
    list_possible_digits = convert_int_tab(n)

    all_combi = [[]]

    for i in range(len(list_possible_digits)):
        # Creating new combination with i as new digit
        new_combi = []

        # For all previous pandigital numbers
        for combi in all_combi:
            # For all positions
            for pos in range(len(combi) + 1):
                # Create a new number
                tmp = list(combi)
                tmp.insert(pos, list_possible_digits[i])
                new_combi.append(tmp)

        all_combi = new_combi

    return all_combi

def gen_comb_number(n):
    """
    Generate all combinations from the digits of n
    """
    list_res = gen_comb_number_tab(n)
    return reduce(lambda l, y: l + [convert_tab_int(y)], list_res, [])

def is_permutation(nb1, nb2):
    """
    Return true if nb1 is a permutation of nb2
    """
    tab_nb2 = convert_int_tab(nb2)

    for d in convert_int_tab(nb1):
        if d in tab_nb2:
            tab_nb2.remove(d)

    return tab_nb2 == []


if __name__ == '__main__':
    print("Testing convert_tab_int function... ", end="")
    assert(convert_tab_int([1]) == 1)
    assert(convert_tab_int([1, 2]) == 12)
    assert(convert_tab_int([1, 2, 3]) == 123)
    assert(convert_tab_int([1, 1, 1]) == 111)
    assert(convert_tab_int([0, 1, 1]) == 11)
    assert(convert_tab_int([0, 1, 0]) == 10)
    print("OK")

    print("Testing convert_int_tab function... ", end="")
    assert(convert_int_tab(1) == [1])
    assert(convert_int_tab(10) == [1, 0])
    assert(convert_int_tab(123) == [1, 2, 3])
    assert(convert_int_tab(1111) == [1, 1, 1, 1])
    print("OK")

    print("Testing gen_comb_pandigital function... ", end="")
    assert(convert_int_tab(7652413) in gen_comb_pandigital(7))
    print("OK")

    print("Testing gen_comb_number_tab function... ", end="")
    list_res = [[1, 2], [2, 1]]
    for tab_number in gen_comb_number_tab(12):
        assert(tab_number in list_res)
        list_res.remove(tab_number)
    assert(list_res == [])
    print("OK")

    print("Testing gen_comb_number function... ", end="")
    list_res = [123, 132, 213, 231, 312, 321]
    for number in gen_comb_number(123):
        assert(number in list_res)
        list_res.remove(number)
    assert(list_res == [])
    print("OK")

    print("Testing is_permutation function...", end="")
    assert(is_permutation(123, 231))
    assert(is_permutation(345, 543))
    assert(is_permutation(12345, 54321))
    assert(is_permutation(3434, 4343))
    assert(not is_permutation(123, 331))
    assert(not is_permutation(123, 232))
    assert(not is_permutation(123, 234))
    assert(not is_permutation(123, 1312))
    print("OK")