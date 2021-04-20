use prime_numbers::prime_numbers::PrimeNumbers;

/// Find the sum of all the primes below
fn find_sum_primes_below_n(number: u64) -> u64 {
    let mut primes   = PrimeNumbers::new();

    primes.compute_prime_number_until(number);

    primes.get_primes()
          .iter()
          .fold(0, |sum, val| sum + val)
}

fn main() {
    let res = find_sum_primes_below_n(2000000);
    println!("{}", res);
}
