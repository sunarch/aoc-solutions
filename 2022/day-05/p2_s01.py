#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 5 / Part 2

https://adventofcode.com/2022/day/5
"""

from p1_s01 import process_input_structure


INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> str:
    """Main"""

    lines_stack = []

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:

        while True:
            line = fh_input.readline().rstrip('\n')
            if line == '':
                break
            lines_stack.append(line)

        stacks = process_input_structure(lines_stack)
        # for i, stack in enumerate(stacks):
        #     print(i, ':', stack)
        # print('-------')

        for line in fh_input:
            instruction_parts = line.rstrip().split()
            count = int(instruction_parts[1])
            source = int(instruction_parts[3]) - 1
            destination = int(instruction_parts[5]) - 1

            split_index = len(stacks[source]) - count
            moved_list = stacks[source][split_index:]
            stacks[source] = stacks[source][:split_index]
            stacks[destination].extend(moved_list)

            # for i, stack in enumerate(stacks):
            #     print(i, ':', stack)
            # print('-------')

    return ''.join([stack[-1] for stack in stacks])


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
