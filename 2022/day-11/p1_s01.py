#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 11 / Part 1

https://adventofcode.com/2022/day/11
"""

from functools import partial
from typing import Generator


INPUT_FILENAME: str = 'input.txt'

ROUNDS = 20


def main(input_filename: str, rounds: int) -> int:
    """Main"""

    monkeys = list(get_input(input_filename))
    # for monkey in monkeys:
    #     print(monkey)

    for _ in range(rounds):
        monkeys = process_monkey_round(monkeys)

    inspection_list = get_sorted_inspection_counts(monkeys)
    # print(inspection_list)
    monkey_business = inspection_list[0] * inspection_list[1]
    return monkey_business


def get_input(filename: str) -> Generator[dict, None, None]:
    """Get input"""

    with open(filename, 'r', encoding='UTF-8') as fh_input:
        monkey_lines = []
        for line in fh_input:
            line = line.rstrip()
            if line == '':
                yield load_monkey(monkey_lines)
                monkey_lines = []
            else:
                monkey_lines.append(line)
        yield load_monkey(monkey_lines)


def operation_plus_old(x):
    """Operation - plus - old"""

    return x + x


def operation_plus_new(x, operand):
    """Operation - plus - new"""

    return x + int(operand)


def operation_mul_old(x):
    """Operation - mul - old"""

    return x * x


def operation_mul_new(x, operand):
    """Operation - mul - new"""

    return x * int(operand)


def load_monkey(monkey_lines: list[str]) -> dict:
    """Load monkey"""

    number = int(monkey_lines[0].lstrip('Monkey ').rstrip(':'))
    starting_items = monkey_lines[1].lstrip('  Starting items: ').split()
    starting_items = [int(item.rstrip(',')) for item in starting_items]
    operator, operand = monkey_lines[2].lstrip('  Operation: new = old ').split()

    match operator:
        case '+':
            if operand == 'old':
                operation = operation_plus_old
            else:
                operation = partial(operation_plus_new, operand=operand)
        case '*':
            if operand == 'old':
                operation = operation_mul_old
            else:
                operation = partial(operation_mul_new, operand=operand)
        case _:
            raise ValueError(f'Operator not recognized: {operator}')

    test_divisible_by = int(monkey_lines[3].lstrip('  Test: divisible by '))
    true_target = int(monkey_lines[4].lstrip('    If true: throw to monkey '))
    false_target = int(monkey_lines[5].lstrip('    If false: throw to monkey '))

    return {
        'number': number,
        'items': starting_items,
        'operation': operation,
        'test divisible by': test_divisible_by,
        'target if true': true_target,
        'target if false': false_target,
        'inspection count': 0
    }


def process_monkey_round(monkeys: list[dict],
                         relief: int = 3,
                         use_alt_relief = False
                         ) -> list[dict]:
    """Process monkey round"""

    for monkey in monkeys:
        while len(monkey['items']) > 0:
            item = monkey['items'].pop(0)
            # inspection
            item = monkey['operation'](item)
            monkey['inspection count'] += 1
            # relief
            if not use_alt_relief:
                item = item // relief

            if item % monkey['test divisible by'] == 0:
                if use_alt_relief:
                    item = item // relief
                monkeys[monkey['target if true']]['items'].append(item)
            else:
                monkeys[monkey['target if false']]['items'].append(item)

    return monkeys


def get_sorted_inspection_counts(monkeys: list[dict]) -> list[int]:
    """Get sorted inspection counts"""

    return list(sorted([monkey['inspection count']
                        for monkey in monkeys],
                       reverse=True))


if __name__ == '__main__':
    print(main(INPUT_FILENAME, ROUNDS))
