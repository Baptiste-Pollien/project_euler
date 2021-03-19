"""
The following iterative sequence is defined for the set of positive
integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz
Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one
million.
"""
from functools import reduce

def compute_length(start, memory):
    """
    Compute the length of collatz sequence with start as first element
    Memory store previous result
    """
    if start in memory:
        return memory[start]
    else:
        if (start % 2 == 0):
            length = compute_length(start // 2, memory) + 1
        else:
            length = compute_length(3*start + 1, memory) + 1

        memory[start] = length

        return length

def longest_chain_under_n(n):
    """
    Return the starting number under n that produce the longest chain.
    """
    max_length = 0
    term_max   = 0

    # Memory to store previous results
    memory = {1: 1}

    for i in range(2, n - 1):
        length = compute_length(i, memory)

        if(length > max_length):
            max_length = length
            term_max = i

    return term_max

if __name__ == '__main__':
    res = longest_chain_under_n(1000000)
    print(res)