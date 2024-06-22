#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 9 / Part 2

https://adventofcode.com/2023/day/9
"""

from typing import Any

from p1_s01 import run, parse_history, calculate_list_differences


INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""
    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        return sum(calculate_previous_value(parse_history(line))
                   for line in fh_input)


def calculate_previous_value(history: list[int]) -> int:
    """Calculate next value in history"""

    if set(history) == {0}:
        return 0

    return history[0] - calculate_previous_value(calculate_list_differences(history))


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
