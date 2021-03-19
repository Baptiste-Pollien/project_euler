"""
A permutation is an ordered arrangement of objects. For example, 3124
is one possible permutation of the digits 1, 2, 3 and 4. If all of
the permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1,
2, 3, 4, 5, 6, 7, 8 and 9?
"""

def fact(n):
    """
    Compute n!
    """
    res = 1

    for i in range(1, n+1):
        res *= i

    return res

def compute_lex_perm():
    """
    Compute and he millionth lexicographic permutation of the digits 0, 1,
    2, 3, 4, 5, 6, 7, 8 and 9
    """
    to_find  = 1000000 - 1
    list_val = [i for i in range(10)]

    for i in range(9, -1, -1):
        start   = to_find // fact(i)
        reste   = to_find % fact(i)
        to_find = reste

        print(list_val[start], end="")

        list_val.remove(list_val[start])

    print()


if __name__ == '__main__':
    compute_lex_perm()
