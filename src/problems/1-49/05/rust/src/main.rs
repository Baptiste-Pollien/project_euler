/// Test if nb is divisible by prime number from 11 to 19
fn is_divisible_prime_20(nb: u64) -> bool{
    let  tab: Vec<u64> = vec![11, 13, 17, 19];

    for i in tab {
        if nb % i != 0 {
            return false;
        }
    }

    true
}

/// Test if nb is divisible by all number from 1 to 20.
fn is_divisible_20(nb: u64) -> bool{
    for i in 1..21 {
        if nb % i != 0 {
            return false;
        }
    }

    return true;
}

/// Find the smallest positive number that is evenly divisible by all
/// of the numbers from 1 to 20
fn find_number_divisible_20() -> u64 {
    // Number divisible by number from 1 to 10
    let divisible_10: u64 = 2520;
    let mut number:   u64 = divisible_10;

    loop {
        if is_divisible_prime_20(number){
            if is_divisible_20(number){
                return number;
            }
        }
        number += divisible_10;
    }
}

fn main() {
    let res = find_number_divisible_20();
    println!("{}", res);
}
