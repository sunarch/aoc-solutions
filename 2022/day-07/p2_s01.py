#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 7 / Part 2

https://adventofcode.com/2022/day/7
"""

from p1_s01 import build_tree, print_nodes, calc_directory_sizes


INPUT_FILENAME: str = 'input.txt'

SPACE_TOTAL = 70000000
SPACE_REQUIRED = 30000000


def main(input_filename: str) -> int:
    """Main"""

    nodes = build_tree(input_filename)
    if __debug__:
        # print_nodes(nodes)
        pass

    directory_sizes = calc_directory_sizes(nodes)
    if __debug__:
        # print_nodes(nodes, directory_sizes)
        # the below 2 display dirs as files!
        print_nodes(directory_sizes, directory_sizes)
        print_nodes(directory_sizes, directory_sizes, min_size=SPACE_REQUIRED)

    space_available = SPACE_TOTAL - directory_sizes['/']
    if __debug__:
        print_usage(space_available, SPACE_TOTAL, 'space available')

    space_missing = SPACE_REQUIRED - space_available
    if __debug__:
        print_usage(space_missing, SPACE_REQUIRED, 'space missing')

    dirs_large_enough = filter(lambda x: x[1] >= space_missing,
                               directory_sizes.items())
    dir_to_be_freed = sorted(dirs_large_enough,
                             key=lambda x: x[1])[0]
    if __debug__:
        print_usage(dir_to_be_freed[1], SPACE_REQUIRED, 'to be freed',
                    comment=dir_to_be_freed[0])

    return dir_to_be_freed[1]


def print_usage(used: int, total: int, text: str = 'space used',
                comment: str = None):
    """Print usage"""

    justify_text = 16
    justify_digits = 10
    print((text + ':').ljust(justify_text, ' '), end=' ')
    print(('{' + f':>{justify_digits},.0f' + '}').format(used), end='')
    print(' / ', end='')
    print(('{' + f':>{justify_digits},.0f' + '}').format(total), end='')
    if comment is not None:
        print(f' ({comment})', end='')
    print('')


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
