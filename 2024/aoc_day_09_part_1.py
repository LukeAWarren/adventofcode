import os
import prettyprinter as pprint
import numpy as np

def load_data(file_name):
    dense_format = np.genfromtxt(file_name, dtype=int, delimiter=1)
    return dense_format

# def get_file_ids(dense_format):
def get_disk_layout(dense_format):
    disk_layout = ""
    file_id = 0
    for ndx in range(0, len(dense_format)):
        if ndx % 2 == 0:
            disk_layout += str(file_id) * dense_format[ndx]
            file_id += 1
        else:
            disk_layout += "." * dense_format[ndx]
    return disk_layout

def get_disk_layout_array(dense_format):
    disk_layout = []
    file_id = 0
    for ndx in range(0, len(dense_format)):
        if ndx % 2 == 0:
            num_blocks = dense_format[ndx]
            for count in range(0, num_blocks):
                disk_layout.append(str(file_id))
            file_id += 1
        else:
            num_blocks = dense_format[ndx]
            for count in range(0, num_blocks):
                disk_layout.append(".")
    return disk_layout

def rearrange_file_blocks(disk_layout):
    disk_layout_array = list(disk_layout)
    disk_size = len(disk_layout_array)
    starting_first_file_pos = 1
    for last_file_pos in range(disk_size - 1, 1, -1):
        last_block = disk_layout_array[last_file_pos]
        print(last_file_pos, starting_first_file_pos)
        if last_file_pos <= starting_first_file_pos:
            break
        if last_block != ".":
            for first_file_pos in range(starting_first_file_pos, last_file_pos):
                first_block = disk_layout_array[first_file_pos]
                if first_block == ".":
                    disk_layout_array[first_file_pos] = last_block
                    disk_layout_array[last_file_pos] = "."
                    starting_first_file_pos = first_file_pos
                    break

    return "".join(disk_layout_array)

def rearrange_file_blocks_array(disk_layout_array):
    disk_layout_array
    disk_size = len(disk_layout_array)
    starting_first_file_pos = 1
    for last_file_pos in range(disk_size - 1, 1, -1):
        last_block = disk_layout_array[last_file_pos]
        print(last_file_pos, starting_first_file_pos)
        if last_file_pos <= starting_first_file_pos:
            break
        if last_block != ".":
            for first_file_pos in range(starting_first_file_pos, last_file_pos):
                first_block = disk_layout_array[first_file_pos]
                if first_block == ".":
                    disk_layout_array[first_file_pos] = last_block
                    disk_layout_array[last_file_pos] = "."
                    starting_first_file_pos = first_file_pos
                    break

    return disk_layout_array

def get_checksum(disk_layout):
    checksum = 0
    disk_array = list(disk_layout)
    for block_pos in range(0, len(disk_array)):
        file_id = disk_array[block_pos]
        if file_id != '.':
            file_id = disk_array[block_pos]
            checksum += block_pos * int(file_id)
    return checksum

def get_checksum_from_disk_layout_array(disk_array):
    checksum = 0
    for block_pos in range(0, len(disk_array)):
        file_id = disk_array[block_pos]
        if file_id != '.':
            file_id = disk_array[block_pos]
            checksum += block_pos * int(file_id)
    return checksum

dense_format = load_data('aoc_day_09_part_1.dat')
# dense_format = load_data('aoc_day_09_part_1_sample.dat')
# dense_format = load_data('aoc_day_09_part_1_test_01.dat')
# dense_format = load_data('aoc_day_09_part_1_test_02.dat')
# dense_format = load_data('aoc_day_09_part_1_test_03.dat')
# print(dense_format)
# disk_layout = get_disk_layout(dense_format)
# print(disk_layout)
disk_layout_array = get_disk_layout_array(dense_format)
# print("".join(disk_layout_array))
# print(disk_layout_array)
# disk_layout = rearrange_file_blocks(disk_layout)
# print(disk_layout)
disk_layout_array = rearrange_file_blocks_array(disk_layout_array)
# print("".join(disk_layout))
# print(disk_layout_array)
# checksum = get_checksum(disk_layout)
# print(checksum)
checksum_from_disk_layout_array = get_checksum_from_disk_layout_array(disk_layout_array)
print(checksum_from_disk_layout_array)
