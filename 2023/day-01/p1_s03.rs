// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/.

// AoC 2023 / Day 1 / Part 1
//
// https://adventofcode.com/2023/day/1

use std::fs::File;
use std::path::Path;
use std::io::{self, BufRead};
use std::str::Chars;
use std::iter::Rev;


const INPUT_FILE_NAME: &str = "input.txt";

const DIGITS: [char; 10] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];


fn main() {
    let mut sum_value: u32 = 0;

    //let path = Path::new(INPUT_FILE_NAME);

    if let Ok(lines) = read_lines(INPUT_FILE_NAME) {
        for line in lines {
            if let Ok(line_content) = line {
                sum_value += calibration_value(line_content);
            }
        }

        print!("{}\n", sum_value);
    }
}


fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
    where P: AsRef<Path> + std::fmt::Display, {

    let file = match File::open(&filename) {
        Err(why) => panic!("couldn't open {}: {}", filename, why),
        Ok(file) => file,
    };

    Ok(io::BufReader::new(file).lines())
}


fn calibration_value(line: String) -> u32 {
    return (first_digit(&line) * 10) + last_digit(&line);
}


fn first_digit(line: &String) -> u32
{
    let line_in_order: Chars = line.chars();

    for character in line_in_order {
        if DIGITS.contains(&character) {
            return match character.to_digit(10) {
                None => panic!("couldn't convert digit: {}", character),
                Some(digit) => digit,
            };
        }
    }

    panic!("no digit found: {}", line);
}


fn last_digit(line: &String) -> u32
{
    let line_in_order: Rev<Chars> = line.chars().rev();

    for character in line_in_order {
        if DIGITS.contains(&character) {
            return match character.to_digit(10) {
                None => panic!("couldn't convert digit: {}", character),
                Some(digit) => digit,
            };
        }
    }

    panic!("no digit found: {}", line);
}
