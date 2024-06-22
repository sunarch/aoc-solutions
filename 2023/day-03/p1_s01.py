#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 3 / Part 1

https://adventofcode.com/2023/day/3
"""

from typing import Union, Generator
from string import digits


INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    return sum(sum(part_numbers) for part_numbers in part_numbers_by_line(input_filename))


def part_numbers_by_line(file_name: str) -> Generator[list[int], None, None]:
    """Part numbers by line"""

    line_prev: Union[str, None] = None
    line_current: Union[str, None] = None
    line_next: Union[str, None] = None

    line_no: int = 0
    finished: bool = False

    with open(file_name, 'r', encoding='UTF-8') as fh_input:

        while not finished:
            if line_prev is None:
                line_next = fh_input.readline().strip()
                line_current = '.' * len(line_next)

            line_prev = line_current
            line_current = line_next
            line_no += 1
            if __debug__:
                line_header: str = f' Line {line_no} '
                print(f'{line_header:=^80}')
            line_next = fh_input.readline().strip()
            if not line_next:
                finished = True
                line_next = '.' * len(line_current)

            yield find_part_numbers(line_prev, line_current, line_next)


def find_part_numbers(line_prev: str, line_current: str, line_next: str) -> list[int]:
    """Find part numbers"""

    part_numbers: list[int] = []

    current_number: str = ''

    character_left: str = '.'
    surrounding_start_index: int = 0

    character_right: str = '.'
    surrounding_end_index: int = 0

    is_finished: bool = False
    has_number: bool = False
    current_index: int = 0

    while True:

        if current_index == len(line_current):
            is_finished = True

            if current_number != '':
                has_number = True

        if has_number:
            characters_top = line_prev[surrounding_start_index:surrounding_end_index + 1]
            characters_bottom = line_next[surrounding_start_index:surrounding_end_index + 1]

            if __debug__:
                print('', characters_top)
                print(character_left, current_number, character_right)
                print('', characters_bottom)

            if is_part_number(character_left, character_right, characters_top, characters_bottom):
                part_numbers.append(int(current_number))

            has_number = False
            current_number = ''
            character_left = character_right
            surrounding_start_index = surrounding_end_index

        if is_finished:
            break

        current_char: str = line_current[current_index]

        if current_char in digits:
            current_number += current_char
            surrounding_end_index = current_index
        else:
            if current_number == '':
                character_left = current_char
                surrounding_start_index = current_index
            else:
                character_right = current_char
                surrounding_end_index = current_index
                has_number = True

        current_index += 1

    return part_numbers


def is_part_number(left: str, right: str, top: str, bottom: str) -> bool:
    """Check if it is a part number"""

    for source in [left, right, top, bottom]:
        source = source.replace('.', '')
        for digit in digits:
            source = source.replace(digit, '')

        if len(source) > 0:
            if __debug__:
                print('    -> is part number')
            return True

    if __debug__:
        print('    -> is NOT part number')
    return False


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
