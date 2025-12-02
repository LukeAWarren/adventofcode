import os
import prettyprinter as pprint
import numpy as np
import copy

def load_data(file_name):
    file = open(file_name)
    line = file.readline()
    stones = [int(x) for x in line.split(' ')]
    file.close()
    return stones

# stones = load_data('aoc_day_11_part_1_sample.dat')
# stones = load_data('aoc_day_11_part_1_sample_2.dat')
stones = load_data('aoc_day_11_part_1.dat')

def split_stones(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            new_stone_str_length = len(stone_str) // 2
            stone1 = stone_str[:new_stone_str_length]
            stone2 = stone_str[new_stone_str_length:]
            new_stones.append(int(stone1))
            new_stones.append(int(stone2))
        else:
            new_stones.append(stone * 2024)
    return new_stones

print("Initial Arrangement:")
print(stones)
sum = 0
for stone in stones:
    sub_stones = [stone]
    for blink in range(25):
        sub_stones = split_stones(sub_stones)
        print(f"{len(sub_stones)} stones after {(blink + 1)} blinks")
    sum += len(sub_stones)
print(f"{sum} stones after {(blink + 1)} blinks")
