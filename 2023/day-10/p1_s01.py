#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 10 / Part 1

https://adventofcode.com/2023/day/10
"""

from enum import Enum
from typing import Any, Callable, TypeVar


INPUT_FILENAME: str = 'input.txt'


class CellType(Enum):
    """Cell type characters"""
    VERTICAL = '|'
    HORIZONTAL = '-'
    NORTH_EAST = 'L'
    NORTH_WEST = 'J'
    SOUTH_WEST = '7'
    SOUTH_EAST = 'F'
    GROUND = '.'
    START = 'S'


class CellTypeVisual(Enum):
    """Visual replacements for cell type characters"""
    VERTICAL = '║'  # U+2551 : Box Drawings Double Vertical
    HORIZONTAL = '═'  # U+2550 : Box Drawings Double Horizontal
    NORTH_EAST = '╚'  # U+255A : Box Drawings Double Up and Right
    NORTH_WEST = '╝'  # U+255D : Box Drawings Double Up and Left
    SOUTH_WEST = '╗'  # U+2557 : Box Drawings Double Down and Left
    SOUTH_EAST = '╔'  # U+2554 : Box Drawings Double Down and Right
    GROUND = '.'
    START = 'S'


class CardinalDirection(Enum):
    """Cardinal directions"""
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'


def main(input_filename: str) -> int:
    """Main"""
    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        grid: list[str] = [line.strip() for line in fh_input]

    if __debug__:
        print_grid(grid)

    starting_position: tuple[int, int] = find_loop_start(grid)
    if __debug__:
        print(starting_position)

    loop_length: int = determine_loop_length(grid, starting_position)
    farthest_point: int = int(loop_length / 2)

    if __debug__:
        print('Farthest point:', farthest_point)

    return farthest_point


def print_grid(grid: list[str]) -> None:
    """Print grid in a more visual way"""

    for row in grid:
        print(row
              .replace(CellType.VERTICAL.value, CellTypeVisual.VERTICAL.value)
              .replace(CellType.HORIZONTAL.value, CellTypeVisual.HORIZONTAL.value)
              .replace(CellType.NORTH_EAST.value, CellTypeVisual.NORTH_EAST.value)
              .replace(CellType.NORTH_WEST.value, CellTypeVisual.NORTH_WEST.value)
              .replace(CellType.SOUTH_WEST.value, CellTypeVisual.SOUTH_WEST.value)
              .replace(CellType.SOUTH_EAST.value, CellTypeVisual.SOUTH_EAST.value)
              .replace(CellType.GROUND.value, CellTypeVisual.GROUND.value)
              )


def find_loop_start(grid: list[str]) -> tuple[int, int]:
    """Find starting position coordinates of the loop"""

    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == CellType.START.value:
                return row_index, col_index

    raise IndexError('Starting position not found in grid')


def determine_starting_type(grid: list[str], position: tuple[int, int]) -> CellType:
    """Determine type of the starting cell"""

    row, col = position
    neighbor_directions: set[CardinalDirection] = set()

    if row != 0:
        if grid[row - 1][col] in {CellType.VERTICAL.value,
                                  CellType.SOUTH_WEST.value,
                                  CellType.SOUTH_EAST.value}:
            neighbor_directions.add(CardinalDirection.NORTH)

    if row != len(grid) - 1:
        if grid[row + 1][col] in {CellType.VERTICAL.value,
                                  CellType.NORTH_EAST.value,
                                  CellType.NORTH_WEST.value}:
            neighbor_directions.add(CardinalDirection.SOUTH)

    if col != 0:
        if grid[row][col - 1] in {CellType.HORIZONTAL.value,
                                  CellType.NORTH_EAST.value,
                                  CellType.SOUTH_EAST.value}:
            neighbor_directions.add(CardinalDirection.WEST)

    if col != len(grid[row]) - 1:
        if grid[row][col + 1] in {CellType.HORIZONTAL.value,
                                  CellType.NORTH_WEST.value,
                                  CellType.SOUTH_WEST.value}:
            neighbor_directions.add(CardinalDirection.EAST)

    if neighbor_directions == {CardinalDirection.NORTH, CardinalDirection.SOUTH}:
        return CellType.VERTICAL
    if neighbor_directions == {CardinalDirection.WEST, CardinalDirection.EAST}:
        return CellType.HORIZONTAL
    if neighbor_directions == {CardinalDirection.NORTH, CardinalDirection.EAST}:
        return CellType.NORTH_EAST
    if neighbor_directions == {CardinalDirection.NORTH, CardinalDirection.WEST}:
        return CellType.NORTH_WEST
    if neighbor_directions == {CardinalDirection.SOUTH, CardinalDirection.WEST}:
        return CellType.SOUTH_WEST
    if neighbor_directions == {CardinalDirection.SOUTH, CardinalDirection.EAST}:
        return CellType.SOUTH_EAST

    raise ValueError('Could not determine type of starting position cell')


def get_neighbors(cell_type: CellType) -> set[CardinalDirection]:
    """Get the two neighbors of a cell"""

    match cell_type:
        case CellType.VERTICAL:
            return {CardinalDirection.NORTH, CardinalDirection.SOUTH}
        case CellType.HORIZONTAL:
            return {CardinalDirection.EAST, CardinalDirection.WEST}
        case CellType.NORTH_EAST:
            return {CardinalDirection.NORTH, CardinalDirection.EAST}
        case CellType.NORTH_WEST:
            return {CardinalDirection.NORTH, CardinalDirection.WEST}
        case CellType.SOUTH_WEST:
            return {CardinalDirection.SOUTH, CardinalDirection.WEST}
        case CellType.SOUTH_EAST:
            return {CardinalDirection.SOUTH, CardinalDirection.EAST}
        case _:
            raise ValueError(f'Neighbors of cell type can not be determined: {cell_type}')


def determine_loop_length(grid: list[str], starting_position: tuple[int, int]) -> int:
    """Determine loop length"""

    length: int = 0

    row, col = starting_position

    height: int = len(grid)
    width: int = len(grid[row])

    current_cell: CellType = determine_starting_type(grid, starting_position)
    if __debug__:
        print('Starting type:', current_cell)
    current_neighbors: set[CardinalDirection] = get_neighbors(current_cell)
    next_direction: CardinalDirection = current_neighbors.pop()
    coming_from: CardinalDirection = where_coming_from(next_direction)

    while True:
        row, col = next_position((row, col), next_direction, height, width)
        length += 1

        current_cell: CellType = to_cell_type(grid[row][col])

        if current_cell == CellType.START:
            break

        current_neighbors: set[CardinalDirection] = get_neighbors(current_cell)
        current_neighbors.remove(coming_from)

        next_direction: CardinalDirection = current_neighbors.pop()

        coming_from: CardinalDirection = where_coming_from(next_direction)

    return length


def where_coming_from(target: CardinalDirection) -> CardinalDirection:
    """Return where going in a direction results in coming from"""

    match target:
        case CardinalDirection.NORTH:
            return CardinalDirection.SOUTH
        case CardinalDirection.SOUTH:
            return CardinalDirection.NORTH
        case CardinalDirection.EAST:
            return CardinalDirection.WEST
        case CardinalDirection.WEST:
            return CardinalDirection.EAST
        case _:
            raise ValueError(f'Unrecognized "coming from" target: {target}')


def next_position(position: tuple[int, int], target: CardinalDirection,
                  height: int, width: int) -> tuple[int, int]:
    """Get next grid location"""

    row, col = position

    match target:
        case CardinalDirection.NORTH:
            row -= 1
        case CardinalDirection.SOUTH:
            row += 1
        case CardinalDirection.WEST:
            col -= 1
        case CardinalDirection.EAST:
            col += 1
        case _:
            raise ValueError(f'Unrecognized target: {target}')

    if not 0 <= row < height:
        raise IndexError(f'Next position out of bounds, row: {row}')

    if not 0 <= col < width:
        raise IndexError(f'Next position out of bounds, col: {col}')

    return row, col


def to_cell_type(character: str) -> CellType:
    """Convert character to cell type"""

    for cell_type in CellType:
        if character == cell_type.value:
            return cell_type

    raise ValueError(f'Unrecognized cell type character: "{character}"')


T = TypeVar('T')


def run(entry_point: Callable[[str], int],
        inputs_and_answers: list[tuple[list[Any], T | None]]
        ) -> None:
    """Run multiple configurations"""

    if __debug__:
        print('=' * 80)

    for input_list, correct_answer in inputs_and_answers:
        result: T = entry_point(*input_list)

        if correct_answer is not None:
            assert result == correct_answer

        print('=' * 80)
        print(', '.join(input_list))
        print(result)
        if __debug__:
            print('=' * 80)

    if not __debug__:
        print('=' * 80)


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
