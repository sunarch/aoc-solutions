#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 9 / Part 1

https://adventofcode.com/2022/day/9
"""

from typing import Generator


INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    current_position_head = (0, 0)
    current_position_tail = (0, 0)
    positions_tail_visited = {current_position_tail}

    for direction, steps in get_input(input_filename):
        for _ in range(steps):
            current_position_head = calc_head_position(current_position_head,
                                                       direction)
            current_position_tail = calc_tail_position(current_position_tail,
                                                       current_position_head)
            positions_tail_visited.add(current_position_tail)

    return len(positions_tail_visited)


def get_input(filename: str) -> Generator[tuple[str, int], None, None]:
    """Get input"""

    with open(filename, 'r', encoding='UTF-8') as fh_input:
        for line in fh_input:
            direction, steps = line.rstrip().split()
            yield direction, int(steps)


def calc_head_position(current_position: tuple[int, int],
                       direction: str
                       ) -> tuple[int, int]:
    """Calculate head position"""

    match direction:
        case 'U':
            movement = (0, 1)
        case 'D':
            movement = (0, -1)
        case 'L':
            movement = (-1, 0)
        case 'R':
            movement = (1, 0)
        case _:
            raise ValueError(f'Direction not recognized: {direction}')
    return add_tuples(current_position, movement)


def calc_tail_position(current_position: tuple[int, int],
                       current_position_head: tuple[int, int]
                       ) -> tuple[int, int]:
    """Calculate tail position"""

    pos_diff = subtract_tuples(current_position_head, current_position)
    pos_diff_abs = abs_tuple(pos_diff)

    if max(pos_diff_abs) == 1:
        return current_position

    return add_tuples(current_position, difference_to_direction(pos_diff))


def add_tuples(tuple_1: tuple, tuple_2: tuple) -> tuple:
    """Add tuples"""

    return tuple(map(sum, zip(tuple_1, tuple_2)))


def subtract_tuples(tuple_1: tuple, tuple_2: tuple) -> tuple:
    """Substract tuples"""

    return tuple(map(lambda x: x[0] - x[1], zip(tuple_1, tuple_2)))


def abs_tuple(input_tuple: tuple):
    """Absolute value in tuple"""

    return tuple(map(abs, input_tuple))


def difference_to_direction(difference: tuple[int, int]) -> tuple:
    """Difference to direction"""

    return tuple(map(number_to_direction, difference))


def number_to_direction(number: int) -> int:
    """Number to direction"""

    if number > 0:
        return 1

    if number < 0:
        return -1

    return 0


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
