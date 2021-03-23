"""
If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

def is_rigth_triangle(a, b, c):
    """
    Return true if the a,b,c triangle is rigth
    """
    return a**2 + b**2 == c**2

def nb_right_triangle(p):
    """
    Return the number of (a, b, c) right triangle
    where a + b + c = p
    """
    nb = 0

    for a in range(1, p // 3 + 1):
        for b in range(1, (p-a)//2 +1):
            c = p - a -b

            if is_rigth_triangle(a, b, c):
                nb += 1

    return nb

def maximised_p_solution(p_sup):
    """
    Find the p that maximised the number of right triangles
    """
    max_nb = 0
    max_p  = 0

    for p in range(1, p_sup):
        nb_rigth_triangle = nb_right_triangle(p)

        if max_nb  < nb_rigth_triangle:
            max_p  = p
            max_nb = nb_rigth_triangle

    return max_p

if __name__ == '__main__':
    res = maximised_p_solution(1000)
    print(res)
