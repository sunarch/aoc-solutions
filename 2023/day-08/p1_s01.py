#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 8 / Part 1

https://adventofcode.com/2023/day/8
"""

from typing import Any, Callable, Generator


INPUT_FILENAME: str = 'input.txt'

NODE_START: str = 'AAA'
NODE_END: str = 'ZZZ'


def main(input_filename: str) -> int:
    """Main"""
    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        directions: str = fh_input.readline().strip()
        _ = fh_input.readline()  # empty line
        pick_next_node = create_node_picker(
            [parse_node(line.strip()) for line in fh_input]
        )

    current_node: str = NODE_START
    steps: int = 0

    for direction in generate_directions(directions):
        current_node = pick_next_node(current_node, direction)
        steps += 1
        if current_node == NODE_END:
            break

    return steps


def parse_node(node_line: str) -> tuple[str, str, str]:
    """Node lines to nodes"""

    name, directions = map(lambda x: x.strip(), node_line.split('='))
    direction_left, direction_right = map(lambda x: x.strip(),
                                          directions.lstrip('(')
                                          .rstrip(')')
                                          .split(','))

    return name, direction_left, direction_right


def create_node_picker(nodes: list[tuple[str, str, str]]) -> Callable[[str, str], str]:
    """Create a closure over the direction dicts to choose next node"""

    left, right = direction_dicts(nodes)

    def wrapper(name: str, direction: str) -> str:
        match direction:
            case 'L':
                return left[name]
            case 'R':
                return right[name]
            case _:
                raise ValueError(f'Unknown direction: {direction}')

    return wrapper


def direction_dicts(nodes: list[tuple[str, str, str]]) -> tuple[dict[str, str], dict[str, str]]:
    """Direction dicts from nodes"""

    left = {}
    right = {}

    for node in nodes:
        name, direction_left, direction_right = node

        left[name] = direction_left
        right[name] = direction_right

    return left, right


def generate_directions(directions: str) -> Generator[str, None, None]:
    """Generate endless directions from directions string"""

    while True:
        for char in directions:
            yield char


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
