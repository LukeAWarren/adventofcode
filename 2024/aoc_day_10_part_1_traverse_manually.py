
import os
import prettyprinter as pprint
import numpy as np

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
    return (second_elevation - first_elevation)

def print_trail_map(trail_map):
    for row in trail_map:
        print("".join(str(x) for x in row))

def print_locations(locations):
    for location in locations:
        print(location)

trail_map = load_data('aoc_day_10_part_1_sample_01.dat')
print_trail_map(trail_map)
trail_heads = find_locations_by_elevation(trail_map, 0)
destinations = find_locations_by_elevation(trail_map, 9)

starting_point = trail_heads[0]
destination = destinations[0]

print(starting_point)
print(destination)

def find_next_moves(trail_map, current_location):
    possible_next_moves = []
    print(f"test: {current_location}")
    # see if we can move up
    if (current_location[0] > 0): # if we're not yet to the first row
        if trail_map[current_location[0] - 1][current_location[1]] - trail_map[current_location[0]][current_location[1]] == 1:
            possible_next_moves.append((current_location[0] - 1, current_location[1]))
    # see if we can move down
    if (current_location[0] < len(trail_map) - 1):  # if we're not yet to the last row
        if trail_map[current_location[0] + 1][current_location[1]] - trail_map[current_location[0]][current_location[1]] == 1:
            possible_next_moves.append((current_location[0] + 1, current_location[1]))
    # see if we can move left
    if (current_location[1] > 0):  # if we're not yet to the first column
        if trail_map[current_location[0]][current_location[1] - 1] - trail_map[current_location[0]][current_location[1]] == 1:
            possible_next_moves.append((current_location[0],current_location[1] - 1))
    # see if we can move right
    if (current_location[1] < len(trail_map[0]) - 1):  # if we're not yet to the last column
        if trail_map[current_location[0]][current_location[1] + 1] - trail_map[current_location[0]][current_location[1]] == 1:
            possible_next_moves.append((current_location[0],current_location[1] + 1))
    pprint.pprint(f"{current_location} can move to {possible_next_moves}")
    return possible_next_moves

next_moves = find_next_moves(trail_map, starting_point)

for next_move in next_moves:
    current_next_moves = find_next_moves(trail_map, next_move)
    for next_next_move in current_next_moves:
        current_current_next_moves = find_next_moves(trail_map, next_next_move)
        for next_next_next_move in current_current_next_moves:
            current_current_current_next_moves = find_next_moves(trail_map, next_next_next_move)
            for next_next_next_next_move in current_current_current_next_moves:
                current_current_current_current_next_moves = find_next_moves(trail_map, next_next_next_next_move)
