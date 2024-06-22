#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2015 / Day 3 / Part 1

https://adventofcode.com/2015/day/3
"""

INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    current_coord: tuple[int, int] = (0, 0)
    visited_coords: set[tuple[int, int]] = {current_coord}

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        while True:
            item = fh_input.read(1)
            if item == '':
                break

            current_coord = move(item, current_coord)
            visited_coords.add(current_coord)

    return len(visited_coords)


def move(direction: str, current_coord: tuple[int, int]) -> tuple[int, int]:
    """Move"""

    match direction:
        case '^':
            return current_coord[0], current_coord[1] + 1
        case 'v':
            return current_coord[0], current_coord[1] - 1
        case '>':
            return current_coord[0] + 1, current_coord[1]
        case '<':
            return current_coord[0] - 1, current_coord[1]
        case _:
            raise ValueError(f'Invalid direction: {direction}')


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
