"""
By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this
problem by trying every route. However, Problem 67, is the same
challenge with a triangle containing one-hundred rows; it cannot be
solved by brute force, and requires a clever method! ;o)
"""

def read_triangle(file_name):
    """
    Read the triangle in the file file_name
    """
    f_triangle = open(file_name, "r")

    triangle = []
    for line_file in f_triangle:
        line = []
        for nb in line_file.split(" "):
            line.append(int(nb))

        triangle.append(line)

    return triangle

def find_max_triangle(file_name):
    """
    Find the maximum total from top to bottom of the triangle in the file
    """
    triangle         = read_triangle(file_name)
    # Compute the max sum for every path
    max_sum_triangle = [[triangle[0][0]]]

    # For every line of the triangle
    for i in range(1, len(triangle)):
        new_line = [max_sum_triangle[i-1][0] + triangle[i][0]]

        # For every number of the line
        for j in range(1, i):
            val1 = max_sum_triangle[i-1][j] + triangle[i][j]
            val2 = max_sum_triangle[i-1][j-1] + triangle[i][j]
            new_line.append(max(val1, val2))

        new_line.append(max_sum_triangle[i-1][i-1] + triangle[i][i])
        max_sum_triangle.append(new_line)

    return max(max_sum_triangle[len(triangle)-1])

if __name__ == '__main__':
    res = find_max_triangle("p067_triangle.txt")
    print(res)