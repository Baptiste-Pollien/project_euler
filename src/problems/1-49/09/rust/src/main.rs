/// Find the product abc, than abc a Pythagorean triplet
/// and a + b + c = 1000
fn find_pythagorean_triplet_1000() -> u64{
    for a in 0..400 as u64 {
        for b in a..400 as u64 {
            let c = ((a * a + b * b) as f64).sqrt() as u64;

            if (a * a + b * b == c * c) && (a + b + c == 1000) {
               return a * b * c
            }
        }
    }

    return 0
}

fn main() {
    let res = find_pythagorean_triplet_1000();
    println!("{}", res);
}
