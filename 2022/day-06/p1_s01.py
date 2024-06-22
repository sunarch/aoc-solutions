#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 6 / Part 1

https://adventofcode.com/2022/day/6
"""

INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    count = 0
    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        last_four = list(fh_input.read(4))
        while True:
            if len(set(last_four)) == 4:
                break
            count += len(last_four.pop(0))
            last_four.append(fh_input.read(1))

        count += len(last_four)

    return count


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
