#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 9 / Part 2

https://adventofcode.com/2022/day/9
"""

from p1_s01 import get_input, calc_head_position, calc_tail_position


INPUT_FILENAME: str = 'input.txt'
KNOT_COUNT = 9


def main(input_filename: str, knot_count: int) -> int:
    """Main"""

    current_position_head = (0, 0)
    current_positions_knots = [(0, 0)] * knot_count
    positions_last_knot_visited = {current_positions_knots[-1]}

    for direction, steps in get_input(input_filename):
        for _ in range(steps):
            current_position_head = calc_head_position(current_position_head,
                                                       direction)
            current_positions_knots[0] = \
                calc_knot_position(current_positions_knots[0],
                                   current_position_head)
            for i_knot in range(1, knot_count):
                current_positions_knots[i_knot] = \
                    calc_knot_position(current_positions_knots[i_knot],
                                       current_positions_knots[i_knot - 1])
            positions_last_knot_visited.add(current_positions_knots[-1])

    return len(positions_last_knot_visited)


def calc_knot_position(current_position: tuple[int, int],
                       current_position_prev: tuple[int, int]
                       ) -> tuple[int, int]:
    """Calculate knot position"""

    return calc_tail_position(current_position, current_position_prev)


if __name__ == '__main__':
    print(main(INPUT_FILENAME, KNOT_COUNT))
