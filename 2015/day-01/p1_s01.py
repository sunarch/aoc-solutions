#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2015 / Day 1 / Part 1

https://adventofcode.com/2015/day/1
"""

INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    current_floor = 0
    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        while True:
            item = fh_input.read(1)
            if item == '':
                break

            if item == '(':
                current_floor += 1
            elif item == ')':
                current_floor -= 1
            else:
                raise ValueError(f'Invalid value in file: {item}')

    return current_floor


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
