#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 10 / Part 2

https://adventofcode.com/2022/day/10
"""

from p1_s01 import get_input


INPUT_FILENAME: str = 'input.txt'

CRT_SIZE = (40, 6)
PIXEL_LIT = '#'
PIXEL_DARK = '.'


def main(input_filename: str, crt_size: tuple[int, int]) -> list[list[str]]:
    """Main"""

    register_x: int = 1
    cpu_cycle: int = 0
    instruction, instruction_arg = None, None
    input_generator = get_input(input_filename)
    crt_display = [['X'] * crt_size[0] for _ in range(crt_size[1])]
    skip_cycle: int = 0

    while True:
        cpu_cycle += 1
        skip_cycle = skip_cycle - 1

        if cpu_cycle > crt_size[0] * crt_size[1]:
            break

        crt_display = update_crt_display(crt_display, crt_size[0],
                                         cpu_cycle, register_x)

        # get new instruction
        if skip_cycle < 0:
            try:
                instruction, instruction_arg = next(input_generator)
            except StopIteration:
                pass

            match instruction:
                case 'noop':
                    if instruction_arg is not None:
                        raise ValueError(f'Argument in "noop": {instruction_arg}')
                    skip_cycle = 0
                case 'addx':
                    if instruction_arg is None:
                        raise ValueError('No argument in "addx"')
                    skip_cycle = 1
                case _:
                    raise ValueError(f'Instruction not recognized: {instruction}')

        # skip cycle if necessary
        if skip_cycle > 0:
            continue

        # execute instruction
        match instruction:
            case 'noop':
                pass
            case 'addx':
                register_x += instruction_arg
            case _:
                raise ValueError(f'Instruction not recognized: {instruction}')

    return crt_display


def update_crt_display(crt_display: list[list[str]],
                       crt_width: int,
                       cpu_cycle: int,
                       register_x: int
                       ) -> list[list[str]]:
    """Update CRT display"""

    crt_column = (cpu_cycle - 1) % crt_width
    crt_row = int((cpu_cycle - crt_column) / crt_width)

    if register_x in range(crt_column - 1, crt_column + 2):
        crt_display[crt_row][crt_column] = PIXEL_LIT
    else:
        crt_display[crt_row][crt_column] = PIXEL_DARK

    return crt_display


def print_crt_display(crt_display: list[list[str]]) -> None:
    """Print CRT display"""

    for row in crt_display:
        print(''.join(row))
    print('')


if __name__ == '__main__':
    print_crt_display(main(INPUT_FILENAME, CRT_SIZE))
