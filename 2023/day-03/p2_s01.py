#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 3 / Part 2

https://adventofcode.com/2023/day/3
"""

from string import digits
from typing import Union, Generator


INPUT_FILENAME: str = 'input.txt'

GEAR_SYMBOL: str = '*'


def main(input_filename: str) -> int:
    """Main"""

    return sum(sum(gear_ratios) for gear_ratios in gear_ratios_by_line(input_filename))


def gear_ratios_by_line(file_name: str) -> Generator[list[int], None, None]:
    """Gear ratios by line"""

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

            yield find_gear_ratios(line_prev, line_current, line_next)


def find_gear_ratios(line_prev: str, line_current: str, line_next: str) -> list[int]:
    """Find gear ratios"""

    gear_ratios: list[int] = []

    current_index: int = 0

    while True:

        if current_index == len(line_current):
            break

        characters_top: str = line_prev[current_index]
        current_char: str = line_current[current_index]
        characters_bottom: str = line_next[current_index]

        if current_index == 0:
            characters_top = '.' + characters_top
            character_left: str = '.'
            characters_bottom = '.' + characters_bottom
        else:
            characters_top = line_prev[current_index - 1] + characters_top
            character_left: str = line_current[current_index - 1]
            characters_bottom = line_next[current_index - 1] + characters_bottom

        if current_index == len(line_current) - 1:
            characters_top = characters_top + '.'
            character_right: str = '.'
            characters_bottom = characters_bottom + '.'
        else:
            characters_top = characters_top + line_prev[current_index + 1]
            character_right: str = line_current[current_index + 1]
            characters_bottom = characters_bottom + line_next[current_index + 1]

        if is_gear(current_char,
                   character_left, character_right,
                   characters_top, characters_bottom):
            gear_ratio = get_gear_ratio(current_index, line_prev, line_current, line_next)
            gear_ratios.append(gear_ratio)

        current_index += 1

    return gear_ratios


def get_gear_ratio(index: int, line_prev: str, line_current: str, line_next: str) -> int:
    """Get gear ratio"""

    if index == 0:
        line_prev = '.' + line_prev
        line_current = '.' + line_current
        line_next = '.' + line_next
        index += 1

    if index == len(line_current) - 1:
        line_prev += '.'
        line_current += '.'
        line_next += '.'
        index = 1

    part_numbers: list[int] = []

    # prev line
    if line_prev[index] in digits:
        part_numbers.append(search_combined(index, line_prev))
    else:
        part_numbers.extend(search_both_sides(index, line_prev))

    # current line
    part_numbers.extend(search_both_sides(index, line_current))

    # next line
    if line_next[index] in digits:
        part_numbers.append(search_combined(index, line_next))
    else:
        part_numbers.extend(search_both_sides(index, line_next))

    if len(part_numbers) != 2:
        raise RuntimeError('Not 2 part numbers at gear')

    if __debug__:
        print('part numbers:', str(part_numbers))

    return part_numbers[0] * part_numbers[1]


def is_gear(char: str, left: str, right: str, top: str, bottom: str) -> bool:
    """Check if char is a gear"""

    if char != GEAR_SYMBOL:
        return False

    if __debug__:
        print('', top)
        print(left, char, right)
        print('', bottom)

    adjacent_parts: int = 0

    for character in [left, right]:
        if character in digits:
            adjacent_parts += 1

    for source in [top, bottom]:
        char_1, char_2, char_3 = source
        if char_2 in digits:
            adjacent_parts += 1
        else:
            for character in [char_1, char_3]:
                if character in digits:
                    adjacent_parts += 1

    if adjacent_parts == 2:
        if __debug__:
            print('    -> is a gear')
        return True

    if __debug__:
        print('    -> is NOT a gear')
    return False


def search_both_sides(index: int, line: str) -> list[int]:
    """Search both sides"""

    part_numbers: list[int] = []

    # left
    part_no = search_backwards(line[0:index])
    if part_no:
        part_numbers.append(int(part_no))

    # right
    part_no = search_forwards(line[index + 1:len(line)])
    if part_no:
        part_numbers.append(int(part_no))

    return part_numbers


def search_combined(index: int, line: str) -> int:
    """Search combined"""

    part_no_1 = search_backwards(line[0:index])
    part_no_2 = search_forwards(line[index:len(line)])
    return int(part_no_1 + part_no_2)


def search_forwards(text: str) -> str:
    """Search forwards"""

    number_string = ''

    for char in text:
        if char in digits:
            number_string += char
        else:
            break

    return number_string


def search_backwards(text: str) -> str:
    """Search backwards"""

    number_string = ''

    for char in text[::-1]:
        if char in digits:
            number_string += char
        else:
            break

    return number_string[::-1]


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
