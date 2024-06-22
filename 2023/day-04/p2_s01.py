#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 4 / Part 2

https://adventofcode.com/2023/day/4
"""

from typing import Iterable

from p1_s01 import parse_ticket


INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        # total tickets
        return sum(cascade_counts(process_winning_numbers(fh_input)))


def cascade_counts(winning_number_counts: list[int]) -> list[int]:
    """Cascade counts"""

    if __debug__:
        print('winning number counts:')
        print(winning_number_counts)

    ticket_counts: list[int] = [1] * len(winning_number_counts)
    if __debug__:
        print('ticket counts:')
        print(ticket_counts)

    for card_index, winning_count in enumerate(winning_number_counts):
        for _ in range(ticket_counts[card_index]):

            for next_index in range(card_index + 1, card_index + 1 + winning_count):
                if next_index < len(ticket_counts):
                    ticket_counts[next_index] += 1

        if __debug__:
            print(ticket_counts)

    return ticket_counts


def process_winning_numbers(lines: Iterable) -> list[int]:
    """Process winning numbers"""

    return [count_winning_numbers(line.strip()) for line in lines]


def count_winning_numbers(line: str) -> int:
    """Count winning numbers"""

    _, winning_numbers, numbers_you_have = parse_ticket(line)

    return len(winning_numbers.intersection(numbers_you_have))


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
