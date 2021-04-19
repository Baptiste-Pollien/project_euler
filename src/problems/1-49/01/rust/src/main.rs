/// Find all the mutliples of 3 or 5 below n
fn multiples_3_5(n: u32) -> u32 {
    let mut sum: u32 = 0;

    for i in 0..n {
        if (i % 3 == 0) || (i % 5 == 0) {
            sum += i;
        }
    }

    sum
}

fn main() {
    let res = multiples_3_5(1000);
    println!("{}", res);
}
