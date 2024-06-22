#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 9 / Part 1

https://adventofcode.com/2023/day/9
"""

from typing import Any, Callable, TypeVar


INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""
    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        return sum(calculate_next_value(parse_history(line))
                   for line in fh_input)


def parse_history(line: str) -> list[int]:
    """Parse history from line"""

    return [int(item) for item in line.split()]


def calculate_next_value(history: list[int]) -> int:
    """Calculate next value in history"""

    if set(history) == {0}:
        return 0

    return history[-1] + calculate_next_value(calculate_list_differences(history))


def calculate_list_differences(original: list[int]) -> list[int]:
    """Calculate the differences between adjacent values in a list"""

    return [b - a for a, b in zip(original[:-1], original[1:])]


T = TypeVar('T')


def run(entry_point: Callable[[str], int],
        inputs_and_answers: list[tuple[list[Any], T | None]]
        ) -> None:
    """Run multiple configurations"""

    if __debug__:
        print('=' * 80)

    for input_list, correct_answer in inputs_and_answers:
        result: T = entry_point(*input_list)

        if correct_answer is not None:
            assert result == correct_answer

        print('=' * 80)
        print(', '.join(input_list))
        print(result)
        if __debug__:
            print('=' * 80)

    if not __debug__:
        print('=' * 80)


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
