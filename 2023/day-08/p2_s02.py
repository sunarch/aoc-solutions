#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 8 / Part 2 / Solution 2

https://adventofcode.com/2023/day/8

TODO: make more optimized version, this takes too long
"""

import sys
from typing import Callable, Generator

from tqdm import tqdm

from p1_s01 import parse_node
from p2_s01 import INPUTS_AND_ANSWERS, is_start_node, is_end_node


INPUT_FILENAME: str = 'input.txt'

INDEX_LEFT: int = 0
INDEX_RIGHT: int = 1


def main(input_filename: str) -> int:
    """Main"""
    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        directions: str = fh_input.readline().strip()
        _ = fh_input.readline()  # empty line
        nodes = [parse_node(line.strip()) for line in fh_input]

    pick_next_node: Callable = create_node_picker(nodes)
    are_all_end_nodes: Callable = create_all_end_node_checker(collect_end_node_names(nodes))

    current_nodes: list[str] = collect_start_node_names(nodes)
    steps: int = 0

    # if __debug__:
    #     print(printable_status(steps, current_nodes))

    for direction in tqdm(generate_directions(directions)):
        for index, node in enumerate(current_nodes):
            current_nodes[index] = pick_next_node(node, direction)

        steps += 1

        # if __debug__:
        #     print(printable_status(steps, current_nodes, direction))

        if are_all_end_nodes(current_nodes):
            break

    return steps


def printable_status(step: int, node_names: list[str], direction: int = 2) -> str:
    """Create printable display of step"""

    return f'Step {step:>10} | Direction: {"LR~"[direction]} | Nodes: {" , ".join(node_names)}'


def collect_start_node_names(nodes: list[tuple[str, str, str]]) -> list[str]:
    """Collect end node names"""

    return [node[0] for node in nodes if is_start_node(node[0])]


def collect_end_node_names(nodes: list[tuple[str, str, str]]) -> set[str]:
    """Collect end node names"""

    return {node[0] for node in nodes if is_end_node(node[0])}


def create_all_end_node_checker(end_nodes: set[str]) -> Callable[[list[str]], bool]:
    """Create a closure over the end nodes to check"""

    def are_all_end_nodes(node_names: list[str]) -> bool:
        """Check if all nodes in list are end nodes"""

        for node_name in node_names:
            if node_name not in end_nodes:
                return False

        return True

    return are_all_end_nodes


def create_node_picker(nodes: list[tuple[str, str, str]]) -> Callable[[str, int], str]:
    """Create a closure over the direction dicts to choose next node"""

    node_names, node_indexes, translation_pairs = translation_dicts(nodes)

    def wrapper(name: str, direction: int) -> str:
        node_index = node_indexes[name]
        translation = translation_pairs[node_index][direction]
        try:
            return node_names[node_index + translation]
        except IndexError:
            print(f'Node picker out of range: "{node_index}" + "{translation}"')
            sys.exit(1)

    return wrapper


def translation_dicts(nodes: list[tuple[str, str, str]]) -> tuple[list[str],
                                                                  dict[str, int],
                                                                  list[tuple[int, int]]]:
    """Direction dicts from nodes"""

    node_names: list[str] = [node[0] for node in nodes]

    node_indexes: dict[str, int] = {}
    left: list[int] = []
    right: list[int] = []

    for index, node in enumerate(nodes):
        name, direction_left, direction_right = node

        node_indexes[name] = index
        left.append(calculate_translation(node_names, index, direction_left))
        right.append(calculate_translation(node_names, index, direction_right))

    return node_names, node_indexes, list(zip(left, right))


def calculate_translation(items: list[str], index_ref: int, target: str) -> int:
    """Calculate translation between two list item positions"""

    index_target = items.index(target)

    if index_ref < index_target:
        return index_target - index_ref

    if index_ref > index_target:
        return (-1) * (index_ref - index_target)

    return 0


def generate_directions(directions: str) -> Generator[int, None, None]:
    """Generate endless directions from directions string"""

    direction_indexes: list[int] = []
    for direction in directions:
        match direction:
            case 'L':
                direction_indexes.append(INDEX_LEFT)
            case 'R':
                direction_indexes.append(INDEX_RIGHT)
            case _:
                raise ValueError(f'Unknown direction: {direction}')

    while True:
        for index in direction_indexes:
            yield index


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
