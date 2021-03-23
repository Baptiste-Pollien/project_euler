"""
Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is
101.

What is the sum of the numbers on the diagonals in a 1001 by 1001
spiral formed in the same way?
"""

def compute_next_radius(radius, start):
    """
    Compte the sum of all the elements on the diag for the radius
    with start as starting point.
    The function also return the end point.
    """
    sum_diag = 4 * start + 20 * radius - 4

    return start + 8 *  radius, sum_diag

def compute_sum_diag(width):
    """
    Compute the sum of the numbers on the diagonals in a
    width by width spiral
    """
    assert(width > 0 and width % 2 == 1)

    radius_max = width // 2 + 1

    tot_sum    = 1
    start      = 2

    for radius in range(1, radius_max):
        start, sum_diag = compute_next_radius(radius, start)
        tot_sum        += sum_diag

    return tot_sum

if __name__ == '__main__':
    res = compute_sum_diag(1001)
    print(res)