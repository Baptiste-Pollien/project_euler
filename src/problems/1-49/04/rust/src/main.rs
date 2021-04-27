/// Generate all palindrome that can be
/// the product of 3-digit numbers.
/// From the greatest to the lowest
fn gen_palindrome_3() -> Vec<u64> {
    let mut list_palindrome = Vec::<u64>::new();

    for i in (0..10).rev() {
        let extern_nb = i * 100001;

        for j in (0..10).rev() {
            let middle_nb = j * 10010;

            for k in (0..10).rev() {
                let palindrome = extern_nb + middle_nb + k * 1100;

                // 10000  = 100 * 100, with 100 min of 3-digit numbers
                // 998001 = 999 * 999, with 999 max of 3-digit numbers
                if 10000 <= palindrome && palindrome <= 998001 {
                    list_palindrome.push(palindrome);
                }
            }
        }
    }

    list_palindrome
}

/// Compute the largest palindrome made from the product of 
/// two 3-digit numbers.
fn largest_palindrome_prod_3_digit_numbers() -> u64{
    // For all 3-digit palindrome
    for p in gen_palindrome_3() {
        let f_p    = p as f64;
        let sqrt_p = (f_p.sqrt() - 1_f64) as u64;
        // For possible divisors of the palindrome
        for div in (sqrt_p)..(p / 100 + 1) {
            let divisors = p / div;
            // Verify that it's the product of two 3-digit numbers
            if 999 >= div 
                && div >= 100 
                &&  p % div == 0 
                && 999 >= divisors 
                && divisors >= 100 {
                return p;
            }
        }
    }
    0
}

fn main() {
    let res = largest_palindrome_prod_3_digit_numbers();
    println!("{}", res);
}
