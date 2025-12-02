
import os
import prettyprinter as pprint
import numpy as np
import copy

def load_data(file_name):
    trail_map = np.genfromtxt(file_name, dtype=int, delimiter=1)
    return trail_map

def find_locations_by_elevation(trail_map, elevation):
    locations = np.where(trail_map == elevation)
    locations_tuples = list(zip(locations[0], locations[1]))
    elevation_locations = []
    for location in locations_tuples:
        x, y = location
        elevation_locations.append((int(x), int(y)))
    return elevation_locations

def elevation_diff(trail_map, first, second):
    first_elevation = trail_map[first[0]][first[1]]
    second_elevation = trail_map[second[0]][second[1]]
    return second_elevation - first_elevation

def print_trail_map(trail_map):
    for row in trail_map:
        print("".join(str(x) for x in row))
    print()

def print_locations(locations):
    for location in locations:
        print(location)

# trail_map = load_data('aoc_day_10_part_1_test_02.dat')
# trail_map = load_data('aoc_day_10_part_1_sample_01.dat')
# trail_map = load_data('aoc_day_10_part_1_sample_02.dat')
trail_map = load_data('aoc_day_10_part_1.dat')

print_trail_map(trail_map)
trail_heads = find_locations_by_elevation(trail_map, 0)
destinations = find_locations_by_elevation(trail_map, 9)

print(f"trail_heads: {trail_heads}")
print(f"destinations: {destinations}")

def find_next_moves(trail_map, current_location, destination):
    valid_moves_for_current_location = []
    global reached_location
    # see if we can move up
    if (current_location[0] > 0): # if we're not yet to the first row
        if trail_map[current_location[0] - 1][current_location[1]] - trail_map[current_location[0]][current_location[1]] == 1:
            print(f"{current_location} can reach {(current_location[0] - 1, current_location[1])}")
            valid_moves_for_current_location.append((current_location[0] - 1, current_location[1]))
    # see if we can move down
    if (current_location[0] < len(trail_map) - 1):  # if we're not yet to the last row
        if trail_map[current_location[0] + 1][current_location[1]] - trail_map[current_location[0]][current_location[1]] == 1:
            valid_moves_for_current_location.append((current_location[0] + 1, current_location[1]))
    # see if we can move left
    if (current_location[1] > 0):  # if we're not yet to the first column
        if trail_map[current_location[0]][current_location[1] - 1] - trail_map[current_location[0]][current_location[1]] == 1:
            valid_moves_for_current_location.append((current_location[0], current_location[1] - 1))
    # see if we can move right
    if (current_location[1] < len(trail_map[0]) - 1):  # if we're not yet to the last column
        if trail_map[current_location[0]][current_location[1] + 1] - trail_map[current_location[0]][current_location[1]] == 1:
            valid_moves_for_current_location.append((current_location[0], current_location[1] + 1))
    if (len(valid_moves_for_current_location) == 0):
        return
    else:
        for location in valid_moves_for_current_location:
            if location == destination:
                reached_location = True
            find_next_moves(trail_map, location, destination)

count = 0

for trail_head in trail_heads:
    for destination in destinations:
        reached_location = False
        find_next_moves(trail_map, trail_head, destination)
        if reached_location == True:
            count += 1

print(count)
