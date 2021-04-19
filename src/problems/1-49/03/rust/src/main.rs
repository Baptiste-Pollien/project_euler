use prime_numbers::prime_numbers::PrimeNumbers;

/// Compute the largest prime factor of the number
fn compute_largest_prime_factor(number: u64) -> u64 {
    let mut primes   = PrimeNumbers::new();
    let mut w_number = number;

    // Current largest prime factor
    let mut largest_pf: u64  = 0;


    for i in 2.. number+1 {
        if primes.is_prime(i) {

            // Test if i is a divisor of number
            if w_number % i == 0 {
                largest_pf   = i;
                w_number     = w_number / i;

                if w_number == 1 {
                    break;
                }
            }
        }
    }
    return largest_pf;
}

fn main() {
    let res = compute_largest_prime_factor(600851475143);
    println!("{}", res);
}
