"""
The n^th term of the sequence of triangle numbers is given by, t_n = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

def char_to_int(c):
    """
    Convert a char to int int value (A = 1)
    """
    return ord(c) - ord('A') + 1

def word_value(word):
    """
    Compute the value of a word
    """
    value = 0

    for c in word:
        value += char_to_int(c)

    return value

def count_triangle_words(file_name):
    """
    Count the number of triangle words in file_name
    """
    f = open(file_name, "r")

    list_names = f.read().replace("\"", '').split(",")

    # Precompute the list of all triangle values
    list_triangles   = [i * (i+1) // 2 for i in range(1, 21)]
    nb_triangle_word = 0

    for word in list_names:

        # Test if the word is a triangle value
        if word_value(word) in list_triangles:
            nb_triangle_word += 1

    return nb_triangle_word

if __name__ == '__main__':
    res = count_triangle_words("p042_words.txt")
    print(res)