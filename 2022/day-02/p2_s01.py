#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 2 / Part 2

https://adventofcode.com/2022/day/2
"""

INPUT_FILENAME: str = 'input.txt'

# Rock, Paper, Scissors
SHAPES = ['A', 'B', 'C']
SCORES_SHAPE = [1, 2, 3]

# draw, lost, won
OUTCOMES = ['Y', 'X', 'Z']
SCORES_OUTCOME = [3, 0, 6]


def main(input_filename: str) -> int:
    """Main"""

    total_score = 0

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        for line in fh_input:
            opponent, outcome = line.rstrip().split()
            # print('opponent:', opponent)

            response = determine_response(opponent, outcome)
            response_score = score_by_value(response, SHAPES, SCORES_SHAPE)
            total_score += response_score
            # print('response:', response, '(', response_score, ')')

            outcome_score = score_by_value(outcome, OUTCOMES, SCORES_OUTCOME)
            total_score += outcome_score
            # print('outcome: ', outcome, '(', outcome_score, ')')

            # print('-------')

    return total_score


def score_by_value(value: str,
                   value_list: list[str, str, str],
                   score_list: list[int, int, int]
                   ) -> int:
    """Score by value"""

    if value not in value_list:
        raise ValueError('Invalid value!')
    score = score_list[value_list.index(value)]
    return score


def determine_response(opponent: str, outcome: str) -> str:
    """Determine response"""

    index_opponent = SHAPES.index(opponent)
    index_outcome = OUTCOMES.index(outcome)
    response = SHAPES[index_opponent - index_outcome]
    return response


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
