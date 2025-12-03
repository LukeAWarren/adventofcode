import os

battery_banks = []

def load_battery_banks(file_name, battery_banks):
    file = open(file_name)
    for battery_bank in file.readlines():
        battery_banks.append(battery_bank)
    file.close()

load_battery_banks('2025/aoc_day_03.dat', battery_banks)

sum_of_joltage = 0

def find_max_joltage(battery_bank):
    max_first_pos = 0
    max_second_pos = 0
    length = len(battery_bank)
    # find max first pos
    max_joltage = 0
    for first_pos in range(0, length - 1):
        for second_pos in range(first_pos + 1, length):
            cur_joltage = int(str(battery_bank[first_pos]) + str(battery_bank[second_pos]))
            if cur_joltage > max_joltage:
                max_joltage = cur_joltage
                max_first_pos = first_pos
                max_second_pos = second_pos
    print(f'{battery_bank[max_first_pos]} + {battery_bank[max_second_pos]} = {max_joltage}')
    return max_joltage

for battery_bank in battery_banks:
    max_joltage = find_max_joltage(list(map(int, battery_bank.rstrip())))
    sum_of_joltage = sum_of_joltage + max_joltage

print(f'sum_of_joltage = {sum_of_joltage}')
