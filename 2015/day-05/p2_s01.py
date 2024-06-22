#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2015 / Day 5 / Part 2

https://adventofcode.com/2015/day/5
"""

INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        # nice count
        return sum(is_nice(line.rstrip()) for line in fh_input)


def is_nice(string: str) -> bool:
    """Main"""

    found_pair_double = False
    found_one_spaced = False

    for i in range(len(string)):

        pair = string[i:i + 2]
        if pair in string[i + 2:]:
            found_pair_double = True

        triplet = f'{string[i:i + 3]:<3}'
        if triplet[0] == triplet[2]:
            found_one_spaced = True

    return found_pair_double and found_one_spaced


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
