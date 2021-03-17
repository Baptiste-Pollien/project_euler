"""
Tool functions to work with numbers : 

- c_tab_int:           Convert a tab of numbers into an integer
- c_int_tab:           Convert an integer to a tab of numbers
- gen_comb_pandigital: Generate all combinations of pandigital 
                       with digits from 1 to n
"""

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

def cc_int_tab(nb):
    """
    Convert an integer to a tab of numbers
    """
    return [int(char) for char in str(nb)]

def gen_comb_pandigital(n):
    """
    Generate all combinations of pandigital with digits from 1 to n
    """
    assert (n >= 1)

    all_combi = [[]]

    for i in range(1, n + 1):
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