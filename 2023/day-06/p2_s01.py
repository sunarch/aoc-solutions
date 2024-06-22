#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 6 / Part 2

https://adventofcode.com/2023/day/6
"""

from p1_s01 import record_bounds, bounds_width


INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        time_total, record = parse_race(*fh_input.readlines()[0:2])

    # possible wins total
    return bounds_width(record_bounds(time_total, record))


def parse_race(line_times: str, line_distances: str) -> tuple[int, int]:
    """Parse race"""

    return parse_data_line(line_times), parse_data_line(line_distances)


def parse_data_line(line: str) -> int:
    """Parse data line"""

    return int(line.strip().split(':')[1].replace(' ', ''))


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
