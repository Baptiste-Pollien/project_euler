"""
A class to compute prime numbers efficiently
"""

class Prime_numbers:
    """
    Class to compute the prime numbers efficiently.
    This class store in a table all prime numbers
    previously computed.
    """

    def __init__(self):
        """
        Initialisation of the table of prime numbers computed.
        """
        # Table of all computed prime numbers
        self.primes = [2, 3]

        # The biggest prime number computed
        # Note : all prime numbers less than max_primes_computed 
        #        are store in primes table
        self.max_primes_computed = 3


    def __test_prime(self, number):
        """
        Test if number is a prime number
        Pre-condition : number <= max_primes_computed
        """
        for nb in self.primes:
            if(nb * nb > number):
                return True
            elif (number % nb == 0):
                return False
        return True

    def compute_prime_number_until(self, number):
        """
        Compute all prime numbers less or equal to number
        Return True if number is a prime number
        """
        if number > self.max_primes_computed:

            for i in range(self.max_primes_computed + 2, number+1, 2):
                if(self.__test_prime(i)):
                    self.primes.append(i)

            self.max_primes_computed = self.primes[-1]

        return number in self.primes

    def get_max_computed_primes(self):
        """
        Return the max computed prime of the object
        """
        return self.max_primes_computed

    def is_prime(self, number):
        """
        Test if number is a prime number
        """
        # Test if the number is divisible by one prime
        # number previously computed
        for nb in self.primes:
            if(nb * nb > number):
                if self.max_primes_computed < number:
                    self.max_primes_computed = number
                self.primes.append(number)
                return True
            elif (number % nb == 0):
                return False


        # If there no divisor was found, test with new divisors
        # until new * new > number
        new = self.next()

        while new * new <= number:
            if (number % new == 0):
                return False

            new = self.next()

        if self.max_primes_computed < number:
                    self.max_primes_computed = number
        self.primes.append(number)

        return True

    def next(self):
        """
        Find the next prime number following max_primes_computed
        """

        # The candidate for the next prime number
        to_test = self.max_primes_computed + 2

        while not self.__test_prime(to_test):
            to_test +=2

        # Update the attibuts of the object
        self.primes.append(to_test)
        self.max_primes_computed = to_test

        return to_test

    def it_primes(self):
        """
        Iterate on all prime numbers
        """
        for prime in self.primes:
            yield prime

        while True:
             yield self.next()


if __name__ == '__main__':
    # If main, tests are launch

    # Tests for compute_prime_number_until function
    print("Testing compute_prime_number_until function... ", end="")
    primes = Prime_numbers()
    assert(primes.compute_prime_number_until(5))
    assert(len(primes.primes) == 3)
    assert(primes.max_primes_computed == 5)

    primes = Prime_numbers()
    assert(primes.compute_prime_number_until(6689))
    assert(primes.max_primes_computed == 6689)
    assert(primes.compute_prime_number_until(6691))
    assert(primes.max_primes_computed == 6691)
    assert(primes.compute_prime_number_until(11))
    assert(primes.compute_prime_number_until(199))
    assert(not primes.compute_prime_number_until(4))
    assert(not primes.compute_prime_number_until(69))
    assert(not primes.compute_prime_number_until(6881))
    assert(primes.compute_prime_number_until(6883))

    primes = Prime_numbers()
    assert(primes.compute_prime_number_until(199))
    assert(199 in primes.primes)
    assert(primes.max_primes_computed == 199)
    print("OK")

    # Tests for is_prime function
    print("Testing is_prime_number function... ", end="")
    primes = Prime_numbers()
    assert(primes.is_prime(5))
    assert(len(primes.primes) == 3)
    assert(primes.max_primes_computed == 5)

    primes = Prime_numbers()
    assert(not primes.is_prime(6881))
    assert(primes.is_prime(6689))
    assert(primes.max_primes_computed == 6689)
    assert(primes.is_prime(6691))
    assert(primes.max_primes_computed == 6691)
    assert(primes.is_prime(11))
    assert(primes.is_prime(199))
    assert(not primes.is_prime(4))
    assert(not primes.is_prime(69))
    assert(primes.is_prime(6883))

    primes = Prime_numbers()
    assert(primes.is_prime(199))
    assert(199 in primes.primes)
    assert(primes.max_primes_computed == 199)
    print("OK")