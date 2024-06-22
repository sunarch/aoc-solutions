#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2015 / Day 3 / Part 2

https://adventofcode.com/2015/day/3
"""

from p1_s01 import move


INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    current_coord_real: tuple[int, int] = (0, 0)
    current_coord_robo: tuple[int, int] = (0, 0)
    visited_coords: set[tuple[int, int]] = {current_coord_real,
                                            current_coord_robo}

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        while True:
            item = fh_input.read(2)
            if item == '':
                break
            item_real, item_robo = item

            current_coord_real = move(item_real, current_coord_real)
            visited_coords.add(current_coord_real)

            current_coord_robo = move(item_robo, current_coord_robo)
            visited_coords.add(current_coord_robo)

    return len(visited_coords)


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
