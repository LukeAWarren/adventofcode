import os

appearances = []
first = []
second = []

def load_locations(file_name, first, second):
    file = open(file_name)    
    for line in file.readlines():
        entries = line.split()        
        first.append(int(entries[0]))
        second.append(int(entries[1]))
    file.close()

def count_appearances(first, second, appearances):
    for i in range(0, len(first)):
        appearance_count = 0
        for j in range(0, len(second)):
            if (first[i] == second[j]):
                appearance_count += 1
        appearances.append(appearance_count)

def similarity_score(first, appearances):
    score = 0
    for ndx in range(0, len(first)):
        score += (first[ndx] * appearances[ndx])
    return score
load_locations('aoc_day_01_part_1.dat', first, second)
count_appearances(first, second, appearances)
score = similarity_score(first, appearances)
print(score)
# sort_locations(first, second)
# compare_location_distance(first, second)
# distance = compare_location_distance(first, second)
# print(distance)