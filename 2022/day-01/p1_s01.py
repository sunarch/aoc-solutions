#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 1 / Part 1

https://adventofcode.com/2022/day/1
"""

INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    max_sum = 0
    current_sum = 0

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        for line in fh_input:
            line = line.rstrip()

            if line == '':
                max_sum = max(max_sum, current_sum)
                current_sum = 0
                continue

            item = int(line)
            current_sum += item

        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
