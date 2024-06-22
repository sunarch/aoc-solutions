#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 2 / Part 2

https://adventofcode.com/2023/day/2
"""

import functools

from p1_s01 import draw_to_values


INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        return power_sum([game_required_cubes(line) for line in fh_input])


def power_sum(cubes_list: list[tuple[int, int, int]]) -> int:
    """Power sum"""

    return sum(cubes_power(cubes) for cubes in cubes_list)


def cubes_power(cubes: tuple[int, int, int]) -> int:
    """Cubes power"""

    return functools.reduce(lambda x, y: x * y, cubes)


def game_required_cubes(line: str) -> tuple[int, int, int]:
    """Game required cubes"""

    _, draws = line.strip().split(':', 1)
    draw_list = draws.split(';')

    required_red: int = 0
    required_green: int = 0
    required_blue: int = 0

    for draw_item in draw_list:
        red, green, blue = draw_to_values(draw_item.strip())
        required_red = max(required_red, red)
        required_green = max(required_green, green)
        required_blue = max(required_blue, blue)

    return required_red, required_green, required_blue


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
