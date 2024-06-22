#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 7 / Part 1

https://adventofcode.com/2022/day/7
"""

INPUT_FILENAME: str = 'input.txt'

MAX_SIZE: int = 100000


def main(input_filename: str) -> int:
    """Main"""

    nodes = build_tree(input_filename)
    # print_nodes(nodes)

    directory_sizes = calc_directory_sizes(nodes)
    # print_nodes(nodes, directory_sizes)
    # the below 2 display dirs as files!
    # print_nodes(directory_sizes, directory_sizes)
    # print_nodes(directory_sizes, directory_sizes, max_size=MAX_SIZE)

    return sum(x[1] for x in directory_sizes.items() if x[1] <= MAX_SIZE)


def build_tree(filename: str):
    """Build tree"""

    root = ''
    current_dir = root
    nodes = {
        '/': -1  # dir
    }

    with open(filename, 'r', encoding='UTF-8') as fh_input:
        for line in fh_input:
            items = line.rstrip().split()

            if items[0] == '$':  # command
                command = items[1]
                if command == 'cd':
                    destination = items[2]

                    if destination == '..':
                        current_dir = current_dir.rsplit('/', 1)[0]
                    elif destination == '/':
                        current_dir = root
                    else:
                        current_dir = f'{current_dir}/{destination}'

                elif command == 'ls':
                    pass

            else:
                type_or_size, name = items

                if type_or_size == 'dir':
                    nodes[f'{current_dir}/{name}'] = -1
                else:
                    nodes[f'{current_dir}/{name}'] = int(type_or_size)

    return nodes


def print_nodes(nodes: dict, sizes: dict = None,
                min_size: int = None, max_size: int = None):
    """Print nodes"""

    print('nodes:')
    for node in sorted(nodes.items(), key=lambda x: x[0]):
        if min_size is not None and node[1] < min_size:
            continue
        if max_size is not None and node[1] > max_size:
            continue
        path_items = node[0].split('/')
        indent = '.' * (len(path_items) - 1) if node[0] != '/' else ''
        name_display = node[0] if node[1] < 0 else f'- {path_items[-1]}'
        type_display = 'dir' if node[1] < 0 else f'file, size={node[1]:,.0f}'
        dir_size = f'(size={sizes[node[0]]:,.0f})' \
                   if sizes is not None and node[0] in sizes \
                   else ''
        print(indent, '-', name_display, f'({type_display})', dir_size)


def calc_directory_sizes(nodes: dict) -> dict:
    """Calculate directory sizes"""

    directory_sizes = {x[0]: 0
                       for x in nodes.items()
                       if x[1] == -1}

    for node in nodes.items():
        if node[1] > -1:
            path_by_dir = ''  # root
            for item in node[0].split('/')[:-1]:
                add_slash = '/' if path_by_dir != '/' else ''
                path_by_dir += add_slash + item
                directory_sizes[path_by_dir] += node[1]

    return directory_sizes


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
