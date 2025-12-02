import os
import prettyprinter as pprint
import numpy as np
import copy
from functools import cache


def load_data(file_name):
    file = open(file_name)
    line = file.readline()
    stones = [int(x) for x in line.split(' ')]
    file.close()
    return stones

# stones = load_data('aoc_day_11_part_1_sample.dat')
# stones = load_data('aoc_day_11_part_2_sample_2.dat')
stones = load_data('aoc_day_11_part_1.dat')

@cache
def count(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return count(1, blinks - 1)
    stone_str = str(stone)
    new_stone_str_length = len(stone_str)
    if new_stone_str_length % 2 == 0:
        stone1 = stone_str[:new_stone_str_length // 2]
        stone2 = stone_str[new_stone_str_length // 2:]
        return count(int(stone1), blinks - 1) + count(int(stone2), blinks - 1)
    else:
        return count(stone * 2024, blinks - 1)
sum = 0
for stone in stones:
    sum += count(stone, 75)

print(f"{sum} stones")
