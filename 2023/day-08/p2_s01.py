#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 8 / Part 2

https://adventofcode.com/2023/day/8

TODO: make more optimized version, this takes too long
"""

from typing import Any, Callable

from tqdm import tqdm

from p1_s01 import parse_node, create_node_picker, generate_directions


INPUT_FILENAME: str = 'input.txt'

START_NODE_LAST_LETTER: str = 'A'
END_NODE_LAST_LETTER: str = 'Z'


def main(input_filename: str) -> int:
    """Main"""
    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        directions: str = fh_input.readline().strip()
        _ = fh_input.readline()  # empty line
        nodes = [parse_node(line.strip()) for line in fh_input]

    pick_next_node: Callable = create_node_picker(nodes)
    current_nodes: list[str] = [node[0] for node in nodes if is_start_node(node[0])]
    steps: int = 0

    if __debug__:
        print(printable_status(steps, current_nodes))

    for direction in tqdm(generate_directions(directions)):
        for index, node in enumerate(current_nodes):
            current_nodes[index] = pick_next_node(node, direction)

        steps += 1

        if __debug__:
            print(printable_status(steps, current_nodes, direction))

        if are_all_end_nodes(current_nodes):
            break

    return steps


def printable_status(step: int, node_names: list[str], direction: str = '~') -> str:
    """Create printable display of step"""

    return f'Step {step:>10} | Direction: {direction} | Nodes: {" , ".join(node_names)}'


def are_all_end_nodes(node_names: list[str]) -> bool:
    """Check if all nodes in list are end nodes"""

    for node_name in node_names:
        if not is_end_node(node_name):
            return False

    return True


def is_start_node(name: str) -> bool:
    """Check if start node"""

    return name[-1] == START_NODE_LAST_LETTER


def is_end_node(name: str) -> bool:
    """Check if end node"""

    return name[-1] == END_NODE_LAST_LETTER


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
