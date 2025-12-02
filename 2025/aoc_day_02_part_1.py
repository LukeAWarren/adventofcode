import os

product_id_ranges = []

def load_ranges(file_name, product_id_ranges):
    file = open(file_name)
    line = file.readline()
    for product_id_range in line.split(','):
        (start, end) = product_id_range.split('-')
        product_id_ranges.append((start, end))
    file.close()

load_ranges('2025/aoc_day_02.dat', product_id_ranges)

invalid_product_ids = set()

def search_product_id_for_repeats(current_product_id, invalid_product_ids):
    length = len(current_product_id)
    if length % 2 == 1: return
    middle_index = int(length / 2)
    # print(f'middle_index: {middle_index}')
    left = current_product_id[:middle_index]
    right = current_product_id[middle_index:]
    # print(f'left: {left}, right: {right}')
    if left == right:
        print(f'current_product_id: {current_product_id}')
        invalid_product_ids.add(current_product_id)

def find_invalid_product_ids(first_product_id, last_product_id, invalid_product_ids):
    for current_product_id in range(int(first_product_id), (int(last_product_id) + 1)):
        search_product_id_for_repeats(str(current_product_id), invalid_product_ids)

for product_id_range in product_id_ranges:
    (first_product_id, last_product_id) = product_id_range
    # print(f'start: {first_product_id}, end: {last_product_id}')
    find_invalid_product_ids(first_product_id, last_product_id, invalid_product_ids)


sum_of_invalid_product_id = 0

for invalid_product_id in invalid_product_ids:
    sum_of_invalid_product_id = sum_of_invalid_product_id + int(invalid_product_id)

print(f'invalid_product_ids = {len(invalid_product_ids)}')
print(f'sum_of_invalid_product_id = {sum_of_invalid_product_id}')
