use prime_numbers::prime_numbers::PrimeNumbers;

/// Find the n th prime number
fn find_n_th_primes(n: usize) -> u64 {
    let mut primes = PrimeNumbers::new();
    let nb_primes  = primes.get_primes().len();

    for _ in nb_primes..n {
        primes.next();
    }

    primes.get_max_primes_computed()
}

fn main() {
    let res = find_n_th_primes(10001);
    println!("{}", res);
}
