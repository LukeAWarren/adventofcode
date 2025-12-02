import os
import prettyprinter as pprint
import numpy as np

def load_data(file_name):
    trail_map = np.genfromtxt(file_name, dtype=int, delimiter=1)
    return trail_map

def find_trail_locations(trail_map, elevation):
    locations = np.where(trail_map == elevation)
    locations_tuples = list(zip(locations[0], locations[1]))
    elevation_locations = []
    for location in locations_tuples:
        x, y = location
        elevation_locations.append((int(x), int(y)))
    return elevation_locations

def trail_head_leads_to_destination(trail_map, trail_head, trail_destination):
    trail_head_x = trail_head[0]
    trail_head_y = trail_head[1]
    trail_destination_x = trail_destination[0]
    trail_destination_y = trail_head[1]

    if (trail_head_x == trail_destination_x and trail_head_y == trail_destination_y):
        return True

    # try left
    if (trail_head_x > 0):
        if trail_head_leads_to_destination(trail_map, (trail_head_x - 1, trail_head_y), trail_destination):
            return True

    # try right
    if (trail_head_x < len(trail_map)):
        if trail_head_leads_to_destination(trail_map, (trail_head_x + 1, trail_head_y), trail_destination):
            return True

    # try up
    if (trail_head_y > 0):
        if trail_head_leads_to_destination(trail_map, (trail_head_x, trail_head_y - 1), trail_destination):
            return True

    # try down
    if (trail_head_y < len(trail_map[0])):
        if trail_head_leads_to_destination(trail_map, (trail_head_x, trail_head_y + 1), trail_destination):
            return True

    return False

trail_map = load_data('aoc_day_10_part_1_test_01.dat')

trail_heads = find_trail_locations(trail_map, 0)
trail_destinations = find_trail_locations(trail_map, 9)
found_destination = trail_head_leads_to_destination(trail_map, (0,0), (9,0))

pprint.pprint(trail_heads)
pprint.pprint(trail_destinations)
pprint.pprint(trail_map)
