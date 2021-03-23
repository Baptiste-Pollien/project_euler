"""
In the United Kingdom the currency is made up of pound (£) and pence
(p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

def compute_nb_possibility_coins():
    """
    Compute how many different ways can £2 be made using any number of coins
    """
    nb = 0

    # 200 coin
    for p in range(0, 2):
        sum200 = p * 200

        # 100 coin
        for o in range(0, 201 - sum200):
            sum100 = sum200 + o * 100

            # 50 coin
            for n in range(0, (200 - sum100)//50 + 1):
                sum50 = sum100 + n * 50

                # 20 coin
                for m in range(0, (200 - sum50) // 20 + 1):
                    sum20 = sum50 + m * 20

                    # 10 coin
                    for l in range(0, (200 - sum20) // 10 + 1):
                        sum10 = sum20 + l * 10

                        # 5 coin
                        for k in range(0, (200 - sum10) // 5 + 1):
                            sum5 = sum10 + k * 5

                            # 2 coin
                            for j in range(0, (200 - sum5) // 2 + 1):
                                sum2 = sum5 + j * 2

                                # 1 coin
                                for i in range(0, (200 - sum2) + 1):
                                    sum = i + j * 2 + k * 5 + l * 10 + m * 20 + n * 50 + o * 100 + p * 200

                                    if sum == 200:
                                        nb += 1
    return nb

if __name__ == '__main__':
    res = compute_nb_possibility_coins()
    print(res)