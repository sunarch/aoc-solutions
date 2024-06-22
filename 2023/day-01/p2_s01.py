#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 1 / Part 2

https://adventofcode.com/2023/day/1
"""

from string import digits


INPUT_FILENAME: str = 'input.txt'

TEXT_DIGIT_PAIRS: tuple[tuple[str, str], ...] = (
        ('one', '1'),
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'),
        ('six', '6'),
        ('seven', '7'),
        ('eight', '8'),
        ('nine', '9')
    )


def main(input_filename: str) -> int:
    """Main"""

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        return sum(calibration_value(line.rstrip()) for line in fh_input)


def calibration_value(line: str) -> int:
    """Calibration value"""

    if __debug__:
        print('line:', line)
    return int(find_digit(line) + find_digit(line, True))


def find_digit(line: str, reverse: bool = False) -> str:
    """Find digit"""

    if __debug__:
        print(' ' * 3, 'find_digit:', end='')

    if reverse:
        line = line[::-1]

    if __debug__:
        print(line, end='')
        if reverse:
            print(' (reversed)')
        else:
            print()

    for index, char in enumerate(line):
        if __debug__:
            print(' ' * 7, '-> index:', index)

        if char in digits:
            if __debug__:
                print(' ' * 7, '-> found number digit:', char)
            return char

        try:
            text_digit = check_text_digit(line[index:], reverse)
        except IndexError:
            pass
        else:
            return text_digit

    raise IndexError(f'No digit: {line}')


def check_text_digit(line: str, reverse: bool = False) -> str:
    """Check text digit"""

    if __debug__:
        print(' ' * 3, 'check_text_digit:', line)

    for text, digit in TEXT_DIGIT_PAIRS:
        if reverse:
            text = text[::-1]

        if line[0:len(text)] == text:
            if __debug__:
                print(' ' * 7, '-> search text:', text, end='')
                if reverse:
                    print(' (reversed)')
                else:
                    print()
                print(' ' * 7, '-> found text digit:', digit)

            return digit

    raise IndexError('No text digit found')


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
