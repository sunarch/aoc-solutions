#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 3 / Part 1

https://adventofcode.com/2022/day/3
"""

INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    sum_priorities = 0

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        for line in fh_input:
            line = line.rstrip()
            half = len(line) // 2
            first, second = line[:half], line[half:]
            # print(line, '->', first, '|', second)
            common = set(first).intersection(set(second)).pop()
            priority = calc_priority(common)
            # print('  =>', common, '(', priority, ')')
            sum_priorities += priority
            # print('-------')

    return sum_priorities


def calc_priority(letter: str) -> int:
    """Calculate priority"""

    letter_no = ord(letter)
    range_small = range(ord('a'), ord('z') + 1)
    if letter_no in range_small:
        offset = ord('a') - 1
    elif letter_no in range(ord('A'), ord('Z') + 1):
        offset = ord('A') - 1 - len(range_small)
    else:
        raise ValueError(f'Invalid letter! - "{letter}"')
    return ord(letter) - offset


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
