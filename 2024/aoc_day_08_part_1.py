import os
import prettyprinter as pprint
import numpy as np

def load_data(file_name):
    origainal_antenna_locations_map = np.genfromtxt(file_name, dtype=str, delimiter=1)
    np.char.strip(origainal_antenna_locations_map)
    return origainal_antenna_locations_map

def find_antenna_locations(origainal_antenna_locations_map, antenna_frequency):
    locations = np.where(origainal_antenna_locations_map == antenna_frequency)
    locations_tuples = list(zip(locations[0], locations[1]))
    antenna_locations = []
    for location in locations_tuples:
        x, y = location
        antenna_locations.append((int(x), int(y)))
    return antenna_locations

def find_frequencies(antenna_locations_map):
    filtered_antenna_frequencies = antenna_locations_map[antenna_locations_map != '.']
    unique_frequencies = np.unique(filtered_antenna_frequencies)
    return unique_frequencies

def find_antenna_distances(antenna_locations, antinode_locations_map):
    map_size = len(antinode_locations_map)
    num_locations = len(antenna_locations)
    for first_index in range(num_locations - 1):
        first_location = antenna_locations[first_index]
        for second_index in range(first_index + 1, num_locations):
            second_location = antenna_locations[second_index]
            print(f"comparing: {first_location} to {second_location}")
            first_x, first_y = first_location
            second_x, second_y = second_location
            dist_x = second_x - first_x
            dist_y = second_y - first_y
            print(f"dist_x: {dist_x}, dist_y: {dist_y}")
            first_antinode_location_x = first_x - dist_x
            first_antinode_location_y = first_y - dist_y
            second_antinode_location_x = second_x + dist_x
            second_antinode_location_y = second_y + dist_y
            print(f"second_antinode_location = {first_antinode_location_x},{first_antinode_location_y}")
            print(f"second_antinode_location = {second_antinode_location_x},{second_antinode_location_y}")

            if (first_antinode_location_x >= 0 and first_antinode_location_x < map_size and
                first_antinode_location_y >= 0 and first_antinode_location_y < map_size):
                antinode_locations_map[first_antinode_location_x][first_antinode_location_y] = '#'
            if (second_antinode_location_x >= 0 and second_antinode_location_x < map_size and
                second_antinode_location_y >= 0 and second_antinode_location_y < map_size):
                antinode_locations_map[second_antinode_location_x][second_antinode_location_y] = '#'

origainal_antenna_locations_map = load_data('aoc_day_08_part_1.dat')
pprint.pprint(origainal_antenna_locations_map)
print()
map_size = len(origainal_antenna_locations_map)
antinode_locations_map = np.full((map_size, map_size), '.')
frequency_list = find_frequencies(origainal_antenna_locations_map)
for frequency in frequency_list:
    antenna_locations = find_antenna_locations(origainal_antenna_locations_map, frequency)
    find_antenna_distances(antenna_locations, antinode_locations_map)

pprint.pprint(antinode_locations_map)

mask = (antinode_locations_map == '#')

print(mask)

count = np.sum(mask)

print(count)


