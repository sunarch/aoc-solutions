#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2015 / Day 2 / Part 2

https://adventofcode.com/2015/day/2
"""

from functools import reduce


INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    total_ribbon = 0
    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        for line in fh_input:
            dimensions = line.rstrip().split('x')
            dimensions = list(map(int, dimensions))
            total_ribbon += ribbon(dimensions) + bow(dimensions)

    return total_ribbon


def ribbon(dimensions: list[int]) -> int:
    """Ribbon"""

    return sum(sorted(dimensions)[0:2] * 2)


def bow(dimensions: list[int]) -> int:
    """Bow"""

    return reduce(lambda x, y: x * y, dimensions)


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
