use prime_numbers::prime_numbers::PrimeNumbers;

/// Find the sum of all the primes below
fn find_sum_primes_below_n(n: u64) -> u64 {
    let mut primes   = PrimeNumbers::new();
}

fn main() {
    let res = find_sum_primes_below_n(2000000);
    println!("{}", res);
}
