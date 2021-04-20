pub mod prime_numbers {

    pub struct PrimeNumbers {
        primes : Vec<u64>,
        max_primes_computed: u64,
    }

    impl PrimeNumbers {
        pub fn new() -> PrimeNumbers {
            PrimeNumbers {
                primes : vec![2, 3],
                max_primes_computed : 3,
            }
        }

        /// Test if number is a prime number
        /// Pre-condition : number <= max_primes_computed
        fn test_prime(&mut self, number: u64) -> bool {
            for nb in &self.primes {
                if nb * nb > number {
                    return true;
                } else if number % nb == 0 {
                    return false;
                }
            }

            return true;
        }

        /// Find the next prime number following max_primes_computed
        fn next(&mut self) -> u64 {
            // The candidate for the next prime number
            let mut to_test = self.max_primes_computed + 2;

            while !self.test_prime(to_test) {
                to_test += 2;
            }

            // Update the attibuts of the object
            self.primes.push(to_test);
            self.max_primes_computed = to_test;

            return to_test;
        }

        /// Test if number is a prime number
        /// This function offers no guarantee for the update of the
        /// max_prime_computed variable
        pub fn is_prime(&mut self, number : u64) -> bool {
            // If number is less or equal of max_primes_computed
            // the result is already computed
            if number <= self.max_primes_computed {
                return self.primes.iter().any(|&nb| nb==number);
            }

            // Test if the number is divisible by one prime
            // number previously computed
            for nb in &self.primes {
                if nb * nb > number {
                    return true;
                } else if number % nb == 0 {
                    return false;
                }
            }

            // If there no divisor was found, test with new divisors
            // until new * new > number
            let mut new = self.next();

            while new * new <= number {
                if number % new == 0 {
                    return false;
                }

                new = self.next()
            }

            return true;
        }

        /// Compute all prime numbers less or equal to number
        /// Return True if number is a prime number
        pub fn compute_prime_number_until(&mut self, number: u64) -> bool {
            if number > self.max_primes_computed {
                for i in ((self.max_primes_computed + 2)
                                ..(number + 1)).step_by(2) {
                    if self.test_prime(i) {
                        self.primes.push(i);
                    }
                }

                if let Some(v) = self.primes.last().copied() {
                    self.max_primes_computed = v;
                }
            }

            return self.primes.iter().any(|&nb| nb==number);
        }

        /// Return a reference on the vector containing
        /// all prime numbers computed
        pub fn get_primes(&self) -> &Vec<u64> {
            &self.primes
        }

        /// Return a reference on the maximum prime number
        /// computed
        pub fn get_max_primes_computed(&self) -> u64 {
            self.max_primes_computed
        }
    }

}

