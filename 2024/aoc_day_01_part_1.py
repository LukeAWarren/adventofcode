import os

first = []
second = []

def load_locations(file_name, first, second):
    file = open(file_name)    
    for line in file.readlines():
        entries = line.split()        
        first.append(int(entries[0]))
        second.append(int(entries[1]))
    file.close()

def sort_locations(first, second):
    first = first.sort()
    second = second.sort()

def compare_location_distance(first, second):
    length = len(first)
    total_distance = 0
    for ndx in range(0, length):
        total_distance += abs(second[ndx] - first[ndx])
    return total_distance

load_locations('aoc_day_01_part_1.dat', first, second)
sort_locations(first, second)
compare_location_distance(first, second)
distance = compare_location_distance(first, second)
print(distance)