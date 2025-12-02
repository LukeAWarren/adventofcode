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

def get_checksum(disk_layout):
    checksum = 0
    disk_array = list(disk_layout)
    for block_pos in range(0, len(disk_array)):
        file_id = disk_array[block_pos]
        if file_id != '.':
            file_id = disk_array[block_pos]
            checksum += block_pos * int(file_id)
    return checksum

# dense_format = load_data('aoc_day_09_part_1.dat')
dense_format = load_data('aoc_day_09_part_1_sample.dat')
# dense_format = load_data('aoc_day_09_part_1_test_01.dat')
disk_layout = get_disk_layout(dense_format)
disk_layout = rearrange_file_blocks(disk_layout)
checksum = get_checksum(disk_layout)
print(checksum)
