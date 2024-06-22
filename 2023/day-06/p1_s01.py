#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 6 / Part 1

https://adventofcode.com/2023/day/6

Equation for the calculation of distance:

-> graphical
distance = (time_total - time_hold) * time_hold
-> graphical - parens resolved
distance = (time_total * time_hold) - (time_hold ** 2)
-> quadratic polynomial
distance = ((-1) * (time_hold ** 2)) + (time_total * time_hold) + 0

This formula can then be used to search for the maximum possible values.
"""

from functools import reduce
from math import sqrt, ceil, floor
from typing import Callable


INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        races: list[tuple[int, int]] = parse_races(*fh_input.readlines()[0:2])
        if __debug__:
            print(races)

    # possible wins total
    return reduce(lambda x, y: x * y,
                  (bounds_width(record_bounds(time_total, record))
                   for time_total, record in races))


def parse_races(line_times: str, line_distances: str) -> list[tuple[int, int]]:
    """Parse races"""

    return list(zip(
        parse_data_line(line_times, 'Time:'),
        parse_data_line(line_distances, 'Distance:')
    ))


def parse_data_line(line: str, title: str) -> list[int]:
    """Parse data line"""

    return [int(item) for item in line.lstrip(title).split() if item != '']


def bounds_width_print(func: Callable) -> Callable:
    """Bounds width - printer"""

    def wrapper(bounds: tuple[int, int]) -> int:
        width = func(bounds)
        if __debug__:
            print('Bounds width:', width)
        return width

    return wrapper


@bounds_width_print
def bounds_width(bounds: tuple[int, int]) -> int:
    """Bounds width"""

    return len(range(*bounds)) + 1


def record_bounds_print(func: Callable) -> Callable:
    """Record bounds - printer"""

    def wrapper(time_total: int, record: int) -> tuple[int, int]:
        if __debug__:
            print('Time:', time_total, '| Record:', record, end='')
        lower, upper = func(time_total, record)
        if __debug__:
            print(f' | Bounds: ({lower}, {upper})')
        return lower, upper

    return wrapper


@record_bounds_print
def record_bounds(time_total: int, record: int) -> tuple[int, int]:
    """Record bounds"""

    quadr_eq_a = -1
    quadr_eq_b = time_total
    quadr_eq_c = (-1) * record

    lower, upper = sorted(quadratic_formula(quadr_eq_a, quadr_eq_b, quadr_eq_c))

    if lower % 1 == 0.0:
        lower += 1.0

    if upper % 1 == 0.0:
        upper -= 1.0

    if __debug__:
        print(f' | Record matches: ({lower}, {upper})', end='')

    return ceil(lower), floor(upper)


def quadratic_formula(a: int, b: int, c: int) -> tuple[float, float]:
    """Quadratic formula

    ((-b) +/- sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    """

    minus_b: int = -b
    b2m4ac: float = sqrt((b ** 2) - (4 * a * c))
    two_a: int = 2 * a

    return (
        (minus_b + b2m4ac) / two_a,
        (minus_b - b2m4ac) / two_a
    )


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
