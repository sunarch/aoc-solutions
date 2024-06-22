#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 8 / Part 2

https://adventofcode.com/2022/day/8
"""

INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    grid = []
    highest_scenic_score = 0

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        for line in fh_input:
            grid.append(list(map(int, list(line.rstrip()))))

        for i_row in range(len(grid)):
            for i_col in range(len(grid[i_row])):
                current = grid[i_row][i_col]
                current_scenic_score = 1

                left = grid[i_row][:i_col]
                value = 0
                for item in reversed(left):
                    if item <= current:
                        value += 1
                    if item >= current:
                        break
                current_scenic_score *= value

                right = grid[i_row][i_col+1:]
                value = 0
                for item in right:
                    if item <= current:
                        value += 1
                    if item >= current:
                        break
                current_scenic_score *= value

                top = [grid[i2_row][i_col]
                       for i2_row in range(0, i_row)]
                value = 0
                for item in reversed(top):
                    if item <= current:
                        value += 1
                    if item >= current:
                        break
                current_scenic_score *= value

                bottom = [grid[i2_row][i_col]
                          for i2_row in range(i_row + 1, len(grid))]
                value = 0
                for item in bottom:
                    if item <= current:
                        value += 1
                    if item >= current:
                        break
                current_scenic_score *= value

                if current_scenic_score > highest_scenic_score:
                    highest_scenic_score = current_scenic_score

    return highest_scenic_score


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
