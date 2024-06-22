#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2015 / Day 4 / Part 2

https://adventofcode.com/2015/day/4
"""

from p1_s01 import main


INPUT_FILENAME: str = 'input.txt'
STARTING_ZEROES: int = 6


if __name__ == '__main__':
    print(main(INPUT_FILENAME, STARTING_ZEROES))
