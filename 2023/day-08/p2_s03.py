#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 8 / Part 2 / Solution 3

https://adventofcode.com/2023/day/8

TODO: make more optimized version, this takes too long
"""

from typing import Callable

from p1_s01 import run, parse_node
from p2_s01 import INPUTS_AND_ANSWERS
from p2_s02 import (INDEX_LEFT, INDEX_RIGHT, create_node_picker,
                    collect_start_node_names, collect_end_node_names)


INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""
    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        directions: str = fh_input.readline().strip()
        _ = fh_input.readline()  # empty line
        nodes = [parse_node(line.strip()) for line in fh_input]

    direction_lookup: Callable = create_direction_lookup(directions)
    pick_next_node: Callable = create_node_picker(nodes)

    end_nodes = collect_end_node_names(nodes)
    check_end_node: Callable = create_end_node_checker(end_nodes)

    current_nodes: list[tuple[int, str]] = [
        (-1, node_name)
        for node_name in collect_start_node_names(nodes)]

    steps = sliding_iterate_nodes(current_nodes,
                                  direction_lookup,
                                  pick_next_node,
                                  check_end_node)

    if __debug__:
        print('Steps:', steps)

    return steps


def sliding_iterate_nodes(current_nodes: list[tuple[int, str]],
                          direction_lookup: Callable,
                          pick_next_node: Callable,
                          check_end_node: Callable
                          ) -> int:
    """Check one node until an end note, and then move on to next"""

    last_index: int = len(current_nodes) - 1

    current_node_pointer: int = 0
    current_bound: int = 0

    while True:
        index, node_name = current_nodes[current_node_pointer]

        index += 1

        if current_node_pointer == 0:
            current_bound = index

        if __debug__:
            print(printable_iteration(
                current_nodes,
                current_node_pointer,
                index,
                node_name,
                current_bound))

        if current_node_pointer > 0 and index > current_bound:
            current_node_pointer -= 1
            continue

        direction = direction_lookup(index)
        next_node = pick_next_node(node_name, direction)

        current_nodes[current_node_pointer] = (index, next_node)

        if current_node_pointer > 0 and index < current_bound:
            continue

        if check_end_node(next_node):
            if current_node_pointer == last_index:
                if __debug__:
                    print('Current nodes:', current_nodes)

                return index + 1

            current_node_pointer += 1


def printable_iteration(current_nodes: list[tuple[int, str]],
                        pointer: int,
                        index: int,
                        node_name: str,
                        current_bound: int
                        ) -> str:
    """Create printable representation of iteration"""

    return_string = f' | Bound: {current_bound}'

    for node_i in range(len(current_nodes)):
        return_string += ' | '

        if node_i != pointer:
            return_string += (' ' * 7)
            continue

        return_string += f'({index}) {node_name}'

    return_string += f' | <-- {str(current_nodes)}'

    return return_string


def create_end_node_checker(end_nodes: set[str]) -> Callable[[str], bool]:
    """Create a closure over the end nodes to check"""

    def check_end_node(node_name: str) -> bool:
        """Check if all nodes in list are end nodes"""

        return node_name in end_nodes

    return check_end_node


def create_direction_lookup(directions: str) -> Callable[[int], int]:
    """Create a function that looks up the direction based on an index"""

    direction_indexes: list[int] = []
    for direction in directions:
        match direction:
            case 'L':
                direction_indexes.append(INDEX_LEFT)
            case 'R':
                direction_indexes.append(INDEX_RIGHT)
            case _:
                raise ValueError(f'Unknown direction: {direction}')

    direction_period = len(direction_indexes)

    def direction_lookup(index: int) -> int:
        """Lookup the direction based on the index"""

        return direction_indexes[index % direction_period]

    return direction_lookup


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
