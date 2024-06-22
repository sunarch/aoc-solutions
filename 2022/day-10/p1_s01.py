#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 10 / Part 1

https://adventofcode.com/2022/day/10
"""

from typing import Generator


INPUT_FILENAME: str = 'input.txt'

WATCHED_CYCLES = [20, 60, 100, 140, 180, 220]


def main(input_filename: str, watched_cycles: list[int]) -> int:
    """Main"""

    register_x = 1
    cpu_cycle = 0
    watched_cycle_values = [0 for _ in watched_cycles]

    for instruction, argument in get_input(input_filename):
        match instruction:

            case 'noop':
                if argument is not None:
                    raise ValueError(f'Argument in "noop": {argument}')
                cpu_cycle += 1
                watched_cycle_values = check_cycle_value(
                    cpu_cycle, register_x,
                    watched_cycles, watched_cycle_values)
                continue

            case 'addx':
                if argument is None:
                    raise ValueError('No argument in "addx"')
                for _ in range(2):
                    cpu_cycle += 1
                    watched_cycle_values = check_cycle_value(
                        cpu_cycle, register_x,
                        watched_cycles, watched_cycle_values)
                register_x += argument

            case _:
                raise ValueError(f'Instruction not recognized: {instruction}')

    # print(list(zip(watched_cycles, watched_cycle_values)))
    return sum(watched_cycle_values)


def get_input(filename: str) -> Generator[tuple[str, int], None, None]:
    """Get input"""

    with open(filename, 'r', encoding='UTF-8') as fh_input:
        for line in fh_input:
            parts = line.rstrip().split()
            instruction = parts[0]
            try:
                argument = int(parts[1])
            except IndexError:
                argument = None
            yield instruction, argument


def check_cycle_value(cpu_cycle: int,
                      register_x: int,
                      watched_cycles: list[int],
                      watched_cycle_values: list[int]) -> list[int]:
    """Check cycle value"""

    if cpu_cycle in watched_cycles:
        watched_cycle_index = watched_cycles.index(cpu_cycle)
        signal_strength = calc_signal_strength(cpu_cycle, register_x)
        watched_cycle_values[watched_cycle_index] = signal_strength

    return watched_cycle_values


def calc_signal_strength(cycle: int, register_x: int) -> int:
    """Calculate signal strength"""

    return cycle * register_x


if __name__ == '__main__':
    print(main(INPUT_FILENAME, WATCHED_CYCLES))
