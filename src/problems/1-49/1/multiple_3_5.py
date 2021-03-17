"""
If we list all the natural numbers below 10 that are multiples of 3
or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from functools import reduce

def multiples_3_5(n):
	"""
	Find all the mutliples of 3 or 5 below n
	"""
	for i in range(n):
		if (i%3==0) or (i%5==0):
			yield i

if __name__ == '__main__':
	res = reduce(lambda n, y: n + y, multiples_3_5(1000), 0)
	print(res)
