"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K
text file containing over five-thousand first names, begin by sorting
it into alphabetical order. Then working out the alphabetical value
for each name, multiply this value by its alphabetical position in
the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
from functools import reduce

def sum_score_name(file_name):
    """
    Compute the sum of the score in the file name
    """
    f = open(file_name, "r")

    list_names = f.read().replace("\"", '').split(",")

    list_names.sort()

    sum_scores = 0

    for pos in range(len(list_names)):
        score = reduce(lambda a,b: 1 + a + (ord(b) - ord('A')), list_names[pos], 0)
        sum_scores += (pos + 1) * score

    return sum_scores

if __name__ == '__main__':
    res = sum_score_name("p022_names.txt")
    print(res)