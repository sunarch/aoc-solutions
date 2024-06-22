#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 4 / Part 1

https://adventofcode.com/2023/day/4
"""

INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        return sum(ticket_to_points(line) for line in fh_input)


def ticket_to_points(line: str):
    """Ticket to points"""

    _, winning_numbers, numbers_you_have = parse_ticket(line)

    return count_points(winning_numbers, numbers_you_have)


def count_points(winning_numbers: set[int], numbers_you_have: set[int]) -> int:
    """Count points"""

    match_count: int = len(winning_numbers.intersection(numbers_you_have))

    return int(2 ** (match_count - 1))


def parse_ticket(line: str) -> tuple[int, set[int], set[int]]:
    """Parse ticket"""

    name_section, numbers_section = line.split(':')
    ticket_no = int(name_section.strip().split()[1])
    numbers_section = numbers_section.strip()

    winning_section, own_section = numbers_section.split('|')

    winning_numbers = parse_number_section(winning_section.strip())
    numbers_you_have = parse_number_section(own_section.strip())

    return ticket_no, winning_numbers, numbers_you_have


def parse_number_section(section: str) -> set[int]:
    """Parse number section"""

    return set(map(lambda x: x.strip(), filter(lambda x: x != '', section.split())))


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
