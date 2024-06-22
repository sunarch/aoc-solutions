#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 12 / Part 1

https://adventofcode.com/2022/day/12

TODO: UNFINISHED
"""

INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    grid = get_input(input_filename)
    steps = 0

    return steps


def get_input(filename: str) -> list[list[str]]:
    """Get input"""

    with open(filename, 'r', encoding='UTF-8') as fh_input:
        grid = []
        for line in fh_input:
            grid.append(list(line.rstrip()))
    return grid


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
