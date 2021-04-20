use prime_numbers::prime_numbers::PrimeNumbers;

fn is_prime_test() {
    // Tests for is_prime function
    print!("Testing is_prime_number function... ");
    let mut primes = PrimeNumbers::new();
    assert!(primes.is_prime(5));

    let mut primes = PrimeNumbers::new();
    assert!(!primes.is_prime(6881));
    assert!(primes.is_prime(6689));
    assert!(primes.is_prime(6691));
    assert!(primes.is_prime(11));
    assert!(primes.is_prime(199));
    assert!(!primes.is_prime(4));
    assert!(!primes.is_prime(69));
    assert!(primes.is_prime(6883));

    let mut primes = PrimeNumbers::new();
    assert!(primes.is_prime(199));
    assert!(!primes.is_prime(0));
    assert!(!primes.is_prime(1));

    let mut primes = PrimeNumbers::new();
    assert!(!primes.is_prime(0));
    assert!(!primes.is_prime(1));

    let mut primes = PrimeNumbers::new();
    assert!(!primes.is_prime(1));
    assert!(!primes.is_prime(6881));
    assert!(primes.is_prime(6689));
    assert!(primes.is_prime(6691));
    assert!(primes.is_prime(11));
    assert!(primes.is_prime(199));
    assert!(!primes.is_prime(4));
    assert!(!primes.is_prime(69));
    assert!(primes.is_prime(6883));
    println!("OK");
}

fn compute_prime_number_until_test() {
    // Tests for compute_prime_number_until function
    print!("Testing compute_prime_number_until function... ");
    let mut primes = PrimeNumbers::new();
    assert!(primes.compute_prime_number_until(5));
    assert!(primes.get_primes().len() == 3);
    assert!(primes.get_max_primes_computed() == 5);

    let mut primes = PrimeNumbers::new();
    assert!(primes.compute_prime_number_until(6689));
    assert!(primes.get_max_primes_computed() == 6689);
    assert!(primes.compute_prime_number_until(6691));
    assert!(primes.get_max_primes_computed() == 6691);
    assert!(primes.compute_prime_number_until(11));
    assert!(primes.compute_prime_number_until(199));
    assert!(!primes.compute_prime_number_until(4));
    assert!(!primes.compute_prime_number_until(69));
    assert!(!primes.compute_prime_number_until(6881));
    assert!(primes.compute_prime_number_until(6883));

    let mut primes = PrimeNumbers::new();
    assert!(primes.compute_prime_number_until(199));
    assert!(primes.get_primes().iter().any(|&nb| nb==199));
    assert!(primes.get_max_primes_computed() == 199);
    println!("OK");
}

fn main() {
    is_prime_test();
    compute_prime_number_until_test();
}
