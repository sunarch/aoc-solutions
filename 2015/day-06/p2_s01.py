#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2015 / Day 6 / Part 2

https://adventofcode.com/2015/day/6

Note: medium runtime
"""

INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    light_values = {}
    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        for line in fh_input:
            direction, corner_1, _, corner_2 = line.rstrip().rsplit(maxsplit=3)
            corner_1 = list(map(int, corner_1.split(',')))
            corner_2 = list(map(int, corner_2.split(',')))
            for i_1 in range(corner_1[0], corner_2[0] + 1):
                for i_2 in range(corner_1[1], corner_2[1] + 1):
                    coord = (i_1, i_2)

                    if direction == 'turn on':
                        value_change = 1
                    elif direction == 'turn off':
                        value_change = -1
                    elif direction == 'toggle':
                        value_change = 2
                    else:
                        raise ValueError(f'Invalid direction: {direction}')

                    try:
                        current_value = light_values[coord]
                    except KeyError:
                        current_value = 0

                    light_values[coord] = max(0, current_value + value_change)

    return sum(light_values.values())


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
