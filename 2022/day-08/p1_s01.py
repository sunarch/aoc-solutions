#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 8 / Part 1

https://adventofcode.com/2022/day/8
"""

INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    grid = []
    visible_count = 0
    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        for line in fh_input:
            grid.append(list(map(int, list(line.rstrip()))))

        # print('grid:')
        # for row in grid:
        #     print(row)

        for i_row in range(len(grid)):
            for i_col in range(len(grid[i_row])):
                current = grid[i_row][i_col]
                # print('current:', current, 'row:', i_row, 'col:', i_col)

                left = grid[i_row][:i_col] + [-1]
                # print('left:', left)
                if max(left) < current:
                    visible_count += 1
                    continue

                right = grid[i_row][i_col+1:] + [-1]
                # print('right:', right)
                if max(right) < current:
                    visible_count += 1
                    continue

                top = [grid[i2_row][i_col]
                       for i2_row in range(0, i_row)] + [-1]
                # print('top:', top)
                if max(top) < current:
                    visible_count += 1
                    continue

                bottom = [grid[i2_row][i_col]
                          for i2_row in range(i_row + 1, len(grid))] + [-1]
                # print('bottom:', bottom)
                if max(bottom) < current:
                    visible_count += 1
                    continue

    return visible_count


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
