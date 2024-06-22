#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 2 / Part 1

https://adventofcode.com/2023/day/2
"""

INPUT_FILENAME: str = 'input.txt'

CUBES_RED: int = 12
CUBES_GREEN: int = 13
CUBES_BLUE: int = 14


def main(input_filename: str) -> int:
    """Main"""

    cubes = (CUBES_RED, CUBES_GREEN, CUBES_BLUE)

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        return sum(game_id_if_possible(line.rstrip(), cubes) for line in fh_input)


def game_id_if_possible(line: str, max_cubes: tuple[int, int, int]) -> int:
    """Game ID if possible"""

    max_red, max_green, max_blue = max_cubes

    game_id, (top_red, top_green, top_blue) = game_id_and_tops(line)

    if top_red <= max_red \
            and top_green <= max_green \
            and top_blue <= max_blue:

        return game_id

    return 0


def game_id_and_tops(line: str) -> tuple[int, tuple[int, int, int]]:
    """Game ID and tops"""

    game_title, draws = line.split(':', 1)
    game_id = int(game_title.split(' ', 1)[1])
    draw_list = draws.split(';')

    top_red: int = 0
    top_green: int = 0
    top_blue: int = 0

    for draw_item in draw_list:
        red, green, blue = draw_to_values(draw_item.strip())
        top_red = max(top_red, red)
        top_green = max(top_green, green)
        top_blue = max(top_blue, blue)

    return game_id, (top_red, top_green, top_blue)


def draw_to_values(text: str) -> tuple[int, int, int]:
    """Draw to values"""

    red: int = 0
    green: int = 0
    blue: int = 0

    for draw_item in text.split(','):
        draw_item = draw_item.strip()
        count, color = draw_item.split()
        count = int(count)
        match color:
            case 'red':
                red = count
            case 'green':
                green = count
            case 'blue':
                blue = count
            case _:
                raise ValueError('Unrecognized color name')

    return red, green, blue


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
