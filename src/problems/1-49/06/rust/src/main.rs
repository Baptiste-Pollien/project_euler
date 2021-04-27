/// Compute the difference between the sum of the squares of the first one
/// n natural numbers and the square of the sum.
fn compute_diff_square_sum(n: u64) -> u64 {
    let mut sum_square: u64 = 0;
    let mut sum_int:    u64 = 0;

    for i in 0..(n + 1){
        sum_square += i*i;
        sum_int    += i;
    }

    sum_int * sum_int - sum_square
}

fn main() {
    let res = compute_diff_square_sum(100);
    println!("{}", res);
}
