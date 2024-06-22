#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 1 / Part 1

https://adventofcode.com/2023/day/1
"""

from string import digits


INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        return sum(calibration_value(line) for line in fh_input)


def calibration_value(line: str) -> int:
    """Calibration value"""

    return int(first_digit(line) + last_digit(line))


def first_digit(line: str) -> str:
    """First digit"""

    for char in line:
        if char in digits:
            return char
    raise IndexError('No digit')


def last_digit(line: str) -> str:
    """Last digit"""

    for char in reversed(line):
        if char in digits:
            return char
    raise IndexError('No digit')


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
