"""
If the numbers 1 to 5 are written out in words: one, two, three,
four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in
total.

If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in
compliance with British usage.
"""

def sum_length_word_1000():
    """
    Return the number of letters for the numbers from 1 to 1000
    """
    # The length of the word corresponding to a number
    nb_length = {
        1 : 3, 2 : 3, 3: 5, 4: 4, 5: 4, 6:3, 7:5, 8:5, 9:4, 
        10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18: 8, 19:8, 20: 6, 
        30 : 6, 40 : 5, 50 : 5, 60 : 5, 70 : 7, 80 : 6, 90 : 6, 100 : 7}

    nb_letters = 0

    # Digits for hundred
    for i in range(0, 10):
        # Digits for tens
        for j in range(0, 10):
            # Digits for units
            for k in range(0, 10):

                # If the number is over hundrer
                if i > 0:
                    nb_letters += nb_length[i] + nb_length[100]

                # i hundred
                if j == 0 and k == 0:
                    continue
                elif i != 0:
                    # and word
                    nb_letters += 3

                # if the number is between 0 and 19
                if 0 <= j and j <= 1:
                    nb_letters += nb_length[j * 10 + k]
                    continue

                # if their an tens number
                if j != 0:
                    nb_letters += nb_length[j*10]

                # If their an unit digit
                if k != 0:
                    nb_letters +=  nb_length[k]

    # + letter for one thousand
    nb_letters += 11
    return nb_letters

if __name__ == '__main__':
    res = sum_length_word_1000()
    print(res)