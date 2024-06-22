#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 10 / Part 2

https://adventofcode.com/2023/day/10

TODO: UNFINISHED
"""

from typing import Any

from p1_s01 import run, print_grid


INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""
    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        grid: list[str] = [line.strip() for line in fh_input]

    if __debug__:
        print_grid(grid)

    return -1


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
