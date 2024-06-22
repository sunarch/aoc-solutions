#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2015 / Day 4 / Part 1

https://adventofcode.com/2015/day/4
"""

from hashlib import md5

INPUT_FILENAME: str = 'input.txt'
STARTING_ZEROES: int = 5


def main(input_filename: str, starting_zeroes: int) -> int:
    """Main"""

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        secret_key = fh_input.readline().rstrip()

    md5_hash = ''
    salt = 0
    start_value = '0' * starting_zeroes
    while md5_hash[0:starting_zeroes] != start_value:
        salt += 1
        value = (secret_key + str(salt)).encode()
        md5_hash = md5(value).hexdigest()
        # if md5_hash[0:1] == '0':
        #     print(value, '-', md5_hash)

    return salt


if __name__ == '__main__':
    print(main(INPUT_FILENAME, STARTING_ZEROES))
