"""
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

# Global variable to store the res of Fibonacci sequence
mem_fibo = {1 : 1, 2 : 1}

def fibo(n):
    """
    Compute Fn
    """
    if not(n in mem_fibo):
        mem_fibo[n] = fibo(n-1) + fibo(n-2)

    return mem_fibo[n]

def compute_index(max_digit):
    """
    Compute the index of the first term in the Fibonacci 
    sequence to contain n digits
    """
    min_number = 10**(max_digit - 1)
    index      = 3

    while (fibo(index) < min_number):
        index += 1

    return index

if __name__ == '__main__':
    res = compute_index(1000)
    print(res)