#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 8 / Part 2 / Solution 4

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

    direction_cycle: int = get_direction_cycle(directions)

    cycle_mapping, end_nodes_in_cycle = analyze_cycle(nodes,
                                                      direction_cycle,
                                                      direction_lookup,
                                                      pick_next_node,
                                                      check_end_node)

    print(nodes)
    print(directions)
    print('End nodes:', end_nodes)
    print('Direction cycle:', direction_cycle)

    #for index, item in enumerate(end_nodes_in_cycle.items()):
    #    name, end_nodes = item
    #    print(index, '|', name, '|', str(end_nodes))

    return

    current_nodes: list[str] = collect_start_node_names(nodes)

    steps = sectioned_iterate_nodes(current_nodes,
                                    direction_cycle,
                                    cycle_mapping,
                                    end_nodes_in_cycle)

    if __debug__:
        print('Steps:', steps)

    return steps


def sectioned_iterate_nodes(current_nodes: list[str],
                            direction_cycle: int,
                            cycle_mapping: dict[str, str],
                            end_nodes_in_cycle: dict[str, set[int]]
                            ) -> int:
    """Check a direction cycle of nodes at a time"""

    print('Direction cycle:', direction_cycle)
    print('Cycle mapping:', cycle_mapping)
    print('End nodes in cycle:', end_nodes_in_cycle)

    cycle_iteration: int = -1

    while True:
        cycle_iteration += 1

        current_cycle_end_nodes: list[set[int]] = [end_nodes_in_cycle[node]
                                                   for node in current_nodes]

        end_node_overlap: set[int] = set.intersection(*current_cycle_end_nodes)

        overlap_size: int = len(end_node_overlap)

        if __debug__:
            print_cycle(cycle_iteration,
                        current_nodes,
                        current_cycle_end_nodes,
                        end_node_overlap,
                        overlap_size)

        if overlap_size > 0:
            done_cycle_total: int = cycle_iteration * direction_cycle
            smallest_overlap_value: int = sorted(end_node_overlap)[0] + 1
            steps: int = done_cycle_total + smallest_overlap_value

            if __debug__:
                print_sectioned_iteration_result(cycle_iteration,
                                                 direction_cycle,
                                                 done_cycle_total,
                                                 smallest_overlap_value,
                                                 steps)

            return steps

        current_nodes = [cycle_mapping[node] for node in current_nodes]


def print_cycle(cycle_iteration: int,
                current_nodes: list[str],
                current_cycle_end_nodes: list[set[int]],
                end_node_overlap: set[int],
                overlap_size: int
                ) -> None:
    """Print cycle details"""

    header: str = f' [ Cycle iteration {cycle_iteration} ] '
    print(f'{header:-^80}')
    print('Current nodes:  ', current_nodes)
    print('Cycle end nodes:', current_cycle_end_nodes)
    if end_node_overlap:
        print('End node overlap:', overlap_size, '~', end_node_overlap)


def print_sectioned_iteration_result(cycle_iteration: int,
                                     direction_cycle: int,
                                     done_cycle_total: int,
                                     smallest_overlap_value: int,
                                     steps: int
                                     ) -> None:
    """Print sectioned iteration result"""

    print(f'{" [ Result ] ":-^80}')

    print(f'Cycle count ({cycle_iteration})'
          f' * Cycle size ({direction_cycle})'
          f' = Cycle total ({done_cycle_total})')

    print(' ' * 3,
          f' + Smallest overlap value ({smallest_overlap_value})', end='')

    print(f' = Steps ({steps})')


def analyze_cycle(nodes: list[tuple[str, str, str]],
                  direction_cycle: int,
                  direction_lookup: Callable,
                  pick_next_node: Callable,
                  check_end_node: Callable
                  ) -> tuple[dict[str, str], dict[str, set[int]]]:
    """Create mapping of one direction cycle"""

    cycle_mapping: dict[str, str] = {node[0]: None for node in nodes}
    end_nodes_in_cycle: dict[str, set[int]] = {node[0]: set() for node in nodes}

    for index, node in enumerate(nodes):
        node_name, _, _ = node
        next_node = node_name

        print(f'{index:>3}', ')', next_node, end='')
        for cycle_index in range(direction_cycle):
            direction = direction_lookup(cycle_index)
            next_node = pick_next_node(next_node, direction)
            print(' ->', next_node, end='')

            if check_end_node(next_node):
                end_nodes_in_cycle[node_name].add(cycle_index)

        cycle_mapping[node_name] = next_node

        print(' |', end_nodes_in_cycle[node_name])
        if end_nodes_in_cycle[node_name]:
            print(node_name, '->', next_node)

    end_nodes_in_cycle = {key: value for key, value in end_nodes_in_cycle.items()
                          if value != set()}

    print('All end nodes union:', set.union(*end_nodes_in_cycle.values()),
          'from', len(end_nodes_in_cycle), 'nodes')

    return cycle_mapping, end_nodes_in_cycle


def create_end_node_checker(end_nodes: set[str]) -> Callable[[str], bool]:
    """Create a closure over the end nodes to check"""

    def check_end_node(node_name: str) -> bool:
        """Check if all nodes in list are end nodes"""

        return node_name in end_nodes

    return check_end_node


def create_direction_lookup(directions: str) -> Callable[[int], int]:
    """Create a function that looks up the direction based on an index"""

    direction_cycle: int = get_direction_cycle(directions)

    direction_indexes: list[int] = []
    for direction in directions:
        match direction:
            case 'L':
                direction_indexes.append(INDEX_LEFT)
            case 'R':
                direction_indexes.append(INDEX_RIGHT)
            case _:
                raise ValueError(f'Unknown direction: {direction}')

    def direction_lookup(index: int) -> int:
        """Lookup the direction based on the index"""

        return direction_indexes[index % direction_cycle]

    return direction_lookup


def get_direction_cycle(directions: str) -> int:
    """Length of a cycle of directions"""

    return len(directions)


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
