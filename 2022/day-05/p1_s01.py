#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 5 / Part 1

https://adventofcode.com/2022/day/5
"""

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

        for line in fh_input:
            instruction_parts = line.rstrip().split()
            count = int(instruction_parts[1])
            source = int(instruction_parts[3]) - 1
            destination = int(instruction_parts[5]) - 1

            for _ in range(count):
                moved_item = stacks[source].pop()
                stacks[destination].append(moved_item)

    return ''.join([stack[-1] for stack in stacks])


def process_input_structure(lines: list[str]) -> list[list[str]]:
    """Process input structure"""

    lines.reverse()
    numbers = lines.pop(0).split()
    stack_count = len(numbers)
    stacks = [[] for _ in range(stack_count)]

    for line in lines:
        for i in range(stack_count):
            index = i * 3 + i
            try:
                item = line[index + 1]
            except IndexError:
                continue
            else:
                if item != ' ':
                    stacks[i].append(item)

    return stacks


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
