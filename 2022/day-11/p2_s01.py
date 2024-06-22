#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 11 / Part 2

https://adventofcode.com/2022/day/11

TODO: UNFINISHED
"""

from functools import reduce

from p1_s01 import get_input, process_monkey_round, get_sorted_inspection_counts


INPUT_FILENAME: str = 'input-example.txt'

ROUNDS = 10000


def main(input_filename: str, rounds: int) -> int:
    """Main"""

    monkeys = list(get_input(input_filename))
    for monkey in monkeys:
        print(monkey)

    relief = reduce(lambda x, y: x * y,
                    [monkey['test divisible by'] for monkey in monkeys])

    for i_round in range(rounds):
        print(i_round)
        monkeys = process_monkey_round(monkeys,
                                       relief=relief,
                                       use_alt_relief=True)
        # for monkey in monkeys:
        #     print(monkey)

    inspection_list = get_sorted_inspection_counts(monkeys)
    # print(inspection_list)
    monkey_business = inspection_list[0] * inspection_list[1]
    return monkey_business


if __name__ == '__main__':
    print(main(INPUT_FILENAME, ROUNDS))
