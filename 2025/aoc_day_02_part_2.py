import os

product_id_ranges = []

def load_ranges(file_name, product_id_ranges):
    file = open(file_name)
    line = file.readline()
    for product_id_range in line.split(','):
        (start, end) = product_id_range.split('-')
        product_id_ranges.append((start, end))
    file.close()

load_ranges('2025/aoc_day_02_temp.dat', product_id_ranges)

invalid_product_ids = set()

LIST_OF_MULITPLES = {
    14 : [7,2,1],
    13 : [1],
    12 : [6, 4, 3, 2, 1],
    11 : [1],
    10 : [5, 2, 1],
    9 : [3, 1],
    8 : [4, 2, 1],
    7 : [1],
    6 : [3, 2, 1],
    5 : [1],
    4 : [2 , 1],
    3 : [1],
    2 : [1]
}

def search_product_id_for_repeats(current_product_id, invalid_product_ids):
    length = len(current_product_id)
    if length <= 1:
        return
    if length > 14:
        raise ("number too big")
    #print(f'current_product_id: {current_product_id}, length: {length}')
    # gotta find all the multiples
    multiples = LIST_OF_MULITPLES[length]
    # print(f'current_product_id: {current_product_id}, length: {length}')
    for multiple in multiples:
        # print(f'    multiple: {multiple}')
        left = current_product_id[:multiple]
        repeats = int(length / multiple)
        cur_str = left * repeats
        if cur_str == current_product_id:
            invalid_product_ids.add(current_product_id)
            return

def find_invalid_product_ids(first_product_id, last_product_id, invalid_product_ids):
    for current_product_id in range(int(first_product_id), (int(last_product_id) + 1)):
        search_product_id_for_repeats(str(current_product_id), invalid_product_ids)

for product_id_range in product_id_ranges:
    (first_product_id, last_product_id) = product_id_range
    # print(f'start: {first_product_id}, end: {last_product_id}')
    find_invalid_product_ids(first_product_id, last_product_id, invalid_product_ids)


sum_of_invalid_product_id = 0

for invalid_product_id in invalid_product_ids:
    print(f'invalid_product_id: {invalid_product_id}')
    sum_of_invalid_product_id = sum_of_invalid_product_id + int(invalid_product_id)

print(f'number of invalid_product_ids = {len(invalid_product_ids)}')
print(f'sum_of_invalid_product_id = {sum_of_invalid_product_id}')
