#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 6 / Part 2

https://adventofcode.com/2022/day/6
"""

INPUT_FILENAME: str = 'input.txt'

UNIQUE_LENGTH = 14


def main(input_filename: str) -> int:
    """Main"""

    count = 0
    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        last_unique = list(fh_input.read(UNIQUE_LENGTH))
        while True:
            if len(set(last_unique)) == UNIQUE_LENGTH:
                break
            count += len(last_unique.pop(0))
            last_unique.append(fh_input.read(1))

        count += len(last_unique)

    return count


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
