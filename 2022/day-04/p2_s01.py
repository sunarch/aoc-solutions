#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 4 / Part 2

https://adventofcode.com/2022/day/4
"""

INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    overlap_count = 0

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        for line in fh_input:
            line = line.rstrip()
            # print(line)

            first, second = line.split(',')
            first_1, first_2 = list(map(int, first.split('-')))
            # print(f'  first:  "{first_1:>2}" | "{first_2:>2}"')
            second_1, second_2 = list(map(int, second.split('-')))
            # print(f'  second: "{second_1:>2}" | "{second_2:>2}"')

            if first_1 <= second_1 <= first_2:
                overlap_count += 1
                # print(f'  => first:    {first_1:>2} || {first_2:>2}')
                # print(f'  => second_1: || {second_1:>2} ||')

            elif first_1 <= second_2 <= first_2:
                overlap_count += 1
                # print(f'  => first:    {first_1:>2} || {first_2:>2}')
                # print(f'  => second_2: || {second_2:>2} ||')

            elif second_1 <= first_1 <= second_2:
                overlap_count += 1
                # print(f'  => second:  {second_1:>2} || {second_2:>2}')
                # print(f'  => first_1: || {first_1:>2} ||')

            elif second_1 <= first_2 <= second_2:
                overlap_count += 1
                # print(f'  => second:  {second_1:>2} || {second_2:>2}')
                # print(f'  => first_2: || {first_2:>2} ||')

            # print('-------')

    return overlap_count


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
