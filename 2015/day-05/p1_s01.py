#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2015 / Day 5 / Part 1

https://adventofcode.com/2015/day/5
"""

INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        # nice count
        return sum(is_nice(line.rstrip()) for line in fh_input)


def is_nice(string: str) -> bool:
    """Is value nice?"""

    forbidden_pair = find_forbidden_pair(string)
    if forbidden_pair is not None:
        # print(string, '- forbidden pair:', forbidden_pair)
        return False

    vowel_count = count_vowels(string)
    if vowel_count < 3:
        # print(string, '- too few vowels:', vowel_count)
        return False

    double = find_double(string)
    if double is not None:
        # print(string, '- OK (vowels:', vowel_count, '| double:', double, ')')
        return True

    # print(string, '- no doubles')
    return False


def find_double(string: str) -> str | None:
    """Find double"""

    for i in range(len(string) - 1):
        pair = string[i:i+2]
        if len(set(pair)) == 1:
            return pair
    return None


def count_vowels(string: str) -> int:
    """Count vowels"""

    return sum(1 for _ in filter(lambda letter: letter in 'aeiou', string))


def find_forbidden_pair(string: str) -> str | None:
    """Find forbidden pair"""

    for pair in ('ab', 'cd', 'pq', 'xy'):
        if pair in string:
            return pair
    return None


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
