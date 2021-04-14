fn fibonacci_even(n: u32) -> u32 {
    // Compute the sum of even fibonnaci terms less than n

    let mut term_n   : u32 = 1;
    let mut term_n_1 : u32 = 2;
    let mut sum_fib  : u32 = 0;

    while term_n_1 < n {
        if term_n_1 % 2 == 0{
            sum_fib += term_n_1;
        }

        // Computing the next term
        let tmp = term_n;
        term_n  = term_n_1;
        term_n_1 = tmp + term_n;
    }

    sum_fib
}

fn main() {
    let res = fibonacci_even(4000000);
    println!("{}", res);
}
