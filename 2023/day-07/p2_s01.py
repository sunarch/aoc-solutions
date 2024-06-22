#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 7 / Part 2

https://adventofcode.com/2023/day/7
"""

from operator import itemgetter
from string import digits
from typing import Any, Generator

from p1_s01 import HandType, HAND_TYPE_TO_NAME, parse_line, determine_hand_type


INPUT_FILENAME: str = 'input.txt'

JOKER: str = 'J'
HIGH_HAND_TYPE_TO_VALUE: dict[str, int] = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,

    'J': 1
}


def main(input_filename: str) -> int:
    """Main"""

    items: list[tuple[tuple[int, Any], int]] = []

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        for line in fh_input:
            hand, bid = parse_line(line)
            items.append((to_sorting_values(hand), bid))

    items = sorted(items, key=itemgetter(0), reverse=True)

    item_count: int = len(items)
    total_winnings: int = 0

    for rank, item in zip(range(item_count, 0, -1), items):
        sorting, bid = item
        winnings = bid * rank

        if __debug__:
            print(printable_entry(rank, bid, winnings, sorting))

        total_winnings += winnings

    return total_winnings


def printable_entry(rank: int, bid: int, winnings: int, sorting_numbers: list[int]) -> str:
    """Printable result entry"""

    return \
        f'Rank: {rank:>4}' + \
        f' | Bid: {bid:>3}' + \
        f' | Winnings: {winnings:>6}' + \
        f' | Cards: {printable_card_faces(sorting_numbers[1:])}' + \
        f' | Type: {HAND_TYPE_TO_NAME[lookup_hand_type(sorting_numbers[0])]}'


def printable_card_faces(card_values: list[int]) -> str:
    """Printable card faces"""

    def card_faces(card_values_inner: list[int]) -> Generator[str, None, None]:
        for value in card_values_inner:
            yield determine_card_face(value), value

    return ' '.join([
        f'{face:>2}' + (
            '   ' if str(face) in digits
            else f'_{value:_>2}'
        )
        for face, value in card_faces(card_values)
    ])


def to_sorting_values(hand: str) -> tuple[int, Any]:
    """Convert hand into sorting values"""

    hand_type_value: int = determine_hand_type(assimilate_jokers(hand)).value
    card_values: list[int] = [determine_card_value(card) for card in list(hand)]

    return hand_type_value, *card_values


def assimilate_jokers(hand: str) -> str:
    """Exchange jokers in hand to most frequent card"""

    card_types: set[str] = set(hand)

    try:
        card_types.remove(JOKER)
    except KeyError:
        pass

    if len(card_types) == 0:
        # there were only jokers
        return hand

    top_card: str = sorted(
        [(x, hand.count(x)) for x in card_types],
        key=itemgetter(1)
    )[-1][0]

    return hand.replace(JOKER, top_card)


def lookup_hand_type(value: int) -> HandType:
    """Reverse-lookup of hand type from value"""

    for item in HandType:
        if item.value == value:
            return item

    raise ValueError(f'Hand type with value "{value}" not found')


def determine_card_value(card: str) -> int:
    """Determine card value"""

    try:
        return HIGH_HAND_TYPE_TO_VALUE[card]
    except KeyError:
        try:
            return int(card)
        except ValueError as err:
            raise ValueError(f'Unrecognized card type: {card}') from err


def determine_card_face(value: int) -> str:
    """Reverse-lookup of card face from value"""

    try:
        return list(HIGH_HAND_TYPE_TO_VALUE.keys())[
            list(HIGH_HAND_TYPE_TO_VALUE.values()).index(value)]
    except ValueError:
        return str(value)


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
