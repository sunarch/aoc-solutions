#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2022 / Day 2 / Part 1

https://adventofcode.com/2022/day/2
"""

INPUT_FILENAME: str = 'input.txt'

# Rock, Paper, Scissors
SHAPES_OPPONENT = ['A', 'B', 'C']
SHAPES_RESPONSE = ['X', 'Y', 'Z']


def main(input_filename: str) -> int:
    """Main"""

    total_score = 0

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        for line in fh_input:
            opponent, response = line.rstrip().split()
            total_score += score_response_shape(response)
            total_score += score_round(opponent, response)

    return total_score


def score_response_shape(shape_response: str) -> int:
    """Score response shape"""

    if shape_response not in SHAPES_RESPONSE:
        raise ValueError('Invalid response shape!')
    scores_shape = [1, 2, 3]  # Rock, Paper, Scissors
    return scores_shape[SHAPES_RESPONSE.index(shape_response)]


def score_round(shape_opponent: str, shape_response: str) -> int:
    """Score round"""

    if shape_opponent not in SHAPES_OPPONENT:
        raise ValueError('Invalid opponent shape!')
    if shape_response not in SHAPES_RESPONSE:
        raise ValueError('Invalid response shape!')
    index_opponent = SHAPES_OPPONENT.index(shape_opponent)
    index_response = SHAPES_RESPONSE.index(shape_response)
    scores_outcome = [3, 0, 6]  # draw, lost, won
    return scores_outcome[index_opponent - index_response]


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
