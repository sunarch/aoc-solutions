#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 1 / Part 2

https://adventofcode.com/2022/day/1
"""

INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    top_three = [0, 0, 0]
    current_sum = 0

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        for line in fh_input:
            line = line.rstrip()

            if line == '':
                top_three = new_top_three(top_three, current_sum)
                current_sum = 0
                continue

            item = int(line)
            current_sum += item

        top_three = new_top_three(top_three, current_sum)

    return sum(top_three)


def new_top_three(top_three: list[int, int, int], new_number: int):
    """New top three"""

    top_three.append(new_number)
    top_three.sort()
    _ = top_three.pop(0)
    return top_three


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
