#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2015 / Day 2 / Part 1

https://adventofcode.com/2015/day/2
"""

INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    total_paper = 0
    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        for line in fh_input:
            dimensions = line.rstrip().split('x')
            dimensions = list(map(int, dimensions))
            length, width, height = dimensions
            total_paper += wrapping_paper(length, width, height)

    return total_paper


def wrapping_paper(length: int,
                   width: int,
                   height: int) -> int:
    """Wrapping paper"""

    return box_area(length, width, height) + \
        extra(length, width, height)


def box_area(length: int, width: int, height: int) -> int:
    """Box area"""

    return 2 * length * width + \
        2 * width * height + \
        2 * height * length


def extra(length: int, width: int, height: int) -> int:
    """Extra"""

    return min([
        length * width,
        width * height,
        height * length
    ])


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
