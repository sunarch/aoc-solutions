#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""AoC 2023 / Day 5 / Part 1

https://adventofcode.com/2023/day/5
"""

from collections.abc import Callable, Iterable
from functools import reduce
from string import digits


INPUT_FILENAME: str = 'input.txt'


def main(input_filename: str) -> int:
    """Main"""

    with open(input_filename, 'r', encoding='UTF-8') as fh_input:
        seeds, conversion_maps = read_almanac(fh_input)

    seed_to_location: Callable[[int], int] = compose(*[create_converter_by_map(map_item)
                                                     for map_item in conversion_maps])

    # closest location
    return min(seed_to_location(seed) for seed in seeds)


def read_almanac(lines: Iterable) -> tuple[list[int], tuple[list[tuple[int, int, int]], ...]]:
    """Read almanac"""

    seeds: list[int] = []
    seed_to_soil_map: list[tuple[int, int, int]] = []
    soil_to_fertilizer_map: list[tuple[int, int, int]] = []
    fertilizer_to_water_map: list[tuple[int, int, int]] = []
    water_to_light_map: list[tuple[int, int, int]] = []
    light_to_temperature_map: list[tuple[int, int, int]] = []
    temperature_to_humidity_map: list[tuple[int, int, int]] = []
    humidity_to_location_map: list[tuple[int, int, int]] = []

    current_header: str = ''

    for line in lines:
        if line.startswith('seeds:'):
            seeds = list(map(int, line.strip().split(':')[1].strip().split()))
            continue

        if line.strip() == '':
            continue

        if line[0] not in digits:
            current_header = line.strip().rstrip(':')
            continue

        conversion: tuple[int, int, int] = tuple(line.strip().split())

        match current_header:
            case 'seed-to-soil map':
                seed_to_soil_map.append(conversion)
            case 'soil-to-fertilizer map':
                soil_to_fertilizer_map.append(conversion)
            case 'fertilizer-to-water map':
                fertilizer_to_water_map.append(conversion)
            case 'water-to-light map':
                water_to_light_map.append(conversion)
            case 'light-to-temperature map':
                light_to_temperature_map.append(conversion)
            case 'temperature-to-humidity map':
                temperature_to_humidity_map.append(conversion)
            case 'humidity-to-location map':
                humidity_to_location_map.append(conversion)
            case _:
                raise ValueError(f'Unrecognized header: "{current_header}"')

    return seeds, (
            seed_to_soil_map,
            soil_to_fertilizer_map,
            fertilizer_to_water_map,
            water_to_light_map,
            light_to_temperature_map,
            temperature_to_humidity_map,
            humidity_to_location_map
        )


def create_converter_by_map(conversion_map: list[tuple[int, int, int]]) -> Callable[[int], int]:
    """Create converter by map"""

    def converter_by_map(value: int) -> int:
        for conversion in conversion_map:
            destination_range_start, source_range_start, range_length = tuple(map(int, conversion))

            if value in range(source_range_start, source_range_start + range_length):
                return destination_range_start + (value - source_range_start)

        return value

    return converter_by_map


def compose(*functions):
    """Compose"""

    return reduce(lambda f, g: lambda x: g(f(x)), functions)


if __name__ == '__main__':
    print(main(INPUT_FILENAME))
