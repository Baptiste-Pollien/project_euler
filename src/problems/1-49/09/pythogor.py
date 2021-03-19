"""
A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c =
1000.
Find the product abc.

"""
from math import sqrt

def find_pythagorean_triplet_1000():
    """
    Find the product abc, than abc a Pythagorean triplet
    and a + b + c = 1000
    """
    for a in range(400):
        for b in range(a, 400):
            c = int(sqrt(a*a + b*b)) 

            if (a*a + b*b == c*c) and (a + b + c == 1000):
               return a*b*c

if __name__ == '__main__':
    res = find_pythagorean_triplet_1000()
    print(res)
