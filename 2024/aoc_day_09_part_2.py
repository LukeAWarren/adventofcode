import os
import prettyprinter as pprint
import numpy as np

def load_data(file_name):
    dense_format = np.genfromtxt(file_name, dtype=int, delimiter=1)
    return dense_format

def get_disk_layout_array(dense_format):
    disk_layout = []
    file_ids = []
    file_id = 0
    for ndx in range(0, len(dense_format)):
        if ndx % 2 == 0:
            num_blocks = dense_format[ndx]
            for count in range(0, num_blocks):
                disk_layout.append(str(file_id))
            file_ids.append(file_id)
            file_id += 1
        else:
            num_blocks = dense_format[ndx]
            for count in range(0, num_blocks):
                disk_layout.append(".")
    return disk_layout, file_ids

def rearrange_file_blocks_array(disk_layout_array, file_ids):
    disk_layout_array
    disk_size = len(disk_layout_array)
    starting_first_file_pos = 1
    mask = (disk_layout_array != '.')
    occupied_disk_layout_array = ['.' if element == '.' else 'x' for element in disk_layout_array]
    occupied_disk_layout_mask = "".join(occupied_disk_layout_array)
    #print("".join(disk_layout_array))
    #print(occupied_disk_layout_mask)
    while(len(file_ids) > 1):
        file_id = file_ids.pop()
        current_file_size = disk_layout_array.count(str(file_id))
        current_file_first_position = disk_layout_array.index(str(file_id))
        print(f"file id: {file_id} is {current_file_size} blocks and first occurs at {current_file_first_position}")
        # i know how big the current file is, now I need to figure out where I can move it to
        # find first location of unoccupied disk big enough for the current file
        search_string = "." * current_file_size
        location = occupied_disk_layout_mask.find(search_string, 0, current_file_first_position)
        if (location == -1):
            continue
        for ndx in range(current_file_size):
            disk_layout_array[location + ndx] = str(file_id)
            disk_layout_array[current_file_first_position + ndx] = "."
        occupied_disk_layout_array = ['.' if element == '.' else 'x' for element in disk_layout_array]
        occupied_disk_layout_mask = "".join(occupied_disk_layout_array)
        # print("".join(disk_layout_array))
        # print(occupied_disk_layout_mask)
    return disk_layout_array

def get_checksum_from_disk_layout_array(disk_array):
    checksum = 0
    for block_pos in range(0, len(disk_array)):
        file_id = disk_array[block_pos]
        if file_id != '.':
            file_id = disk_array[block_pos]
            checksum += block_pos * int(file_id)
    return checksum

dense_format = load_data('aoc_day_09_part_2.dat')
# dense_format = load_data('aoc_day_09_part_2_sample.dat')
# dense_format = load_data('aoc_day_09_part_2_test_01.dat')
# dense_format = load_data('aoc_day_09_part_2_test_02.dat')
# dense_format = load_data('aoc_day_09_part_2_test_03.dat')
# print(dense_format)

disk_layout_array, file_ids = get_disk_layout_array(dense_format)
# print(disk_layout_array)
# print("".join(disk_layout_array))
disk_layout_array = rearrange_file_blocks_array(disk_layout_array, file_ids)
# print("".join(disk_layout_array))
# print(disk_layout_array)
checksum_from_disk_layout_array = get_checksum_from_disk_layout_array(disk_layout_array)
print(checksum_from_disk_layout_array)
