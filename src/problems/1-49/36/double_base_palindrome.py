"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic 
in both bases.

Find the sum of all numbers, less than one million, which are 
palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not i
nclude leading zeros.)
"""

def is_binary_palindromic(n):
    """
    Return true if n is palindromic in base 2
    """
    binary_nb      = bin(n)[2:]
    l              = len(binary_nb)
    is_palindromic = True

    for i in range(l //2):
        is_palindromic = is_palindromic and (binary_nb[i] == binary_nb[l-i-1])

    return is_palindromic

def generate_combination(n):
    """
    Generate all combination of digit of size n
    """
    tab_combi = [[]]
    tab_combi.append([[i] for i in range(1, 10)])

    for i in range(1, n):
        new_tab = []

        for combi in tab_combi[i]:
            for j in range(10):
                tmp = list(combi)
                tmp.append(j)
                new_tab.append(tmp)

        tab_combi.append(new_tab)

    return tab_combi

def generate_palindrome(combi, n):
    """
    Generate a palindorme of size n with the combi
    """
    min = 1
    max = 10**(n-1)
    nb = 0
    for i in range(n // 2):
        nb += (min + max) * combi[i]
        min *= 10
        max //= 10

    if n % 2 == 1:
        nb += min * combi[n // 2]
    return nb

def sum_palindromic_base_10_2():
    """
    Find the sum of all numbers, less than one million, which are 
    palindromic in base 10 and base 2
    """
    sum_palindromic = 0
    size_max        = 6
    tab_combi       = generate_combination(3)

    for i in range(1, size_max + 1):
        for combi in tab_combi[i//2 + i%2]:
            p = generate_palindrome(combi, i)

            if (is_binary_palindromic(p)):
                sum_palindromic += p

    return sum_palindromic

if __name__ == '__main__':
    res = sum_palindromic_base_10_2()
    print(res)