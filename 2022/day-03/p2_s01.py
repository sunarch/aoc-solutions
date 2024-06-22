#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 3 / Part 2

https://adventofcode.com/2022/day/3
"""


from p1_s01 import calc_priority


INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    sum_priorities = 0
    group = []

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        for line in fh_input:
            line = line.rstrip()
            group.append(line)

            if len(group) < 3:
                continue

            sum_priorities += calc_group_priority(group)
            group = []

    return sum_priorities


def calc_group_priority(group: list[str, str, str]) -> int:
    """Calculate group priority"""

    # print(group[0], '|', group[1], '|', group[2])
    group = list(map(set, group))
    common = group[0].intersection(group[1]).intersection(group[2]).pop()
    priority = calc_priority(common)
    # print('  =>', common, '(', priority, ')')
    # print('-------')
    return priority


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
