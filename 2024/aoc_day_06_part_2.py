import os
import copy

DIR_UP = '^'
DIR_RIGHT = '>'
DIR_DOWN = 'v'
DIR_LEFT = '<'
VISITED_MARKER = 'X'
OBSTRUCTION_MARKER = '#'
LOOP_CHECK_MARKER = 'O'

def load_data(file_name):
    map = []
    file = open(file_name)
    for line in file.readlines():
        row = list(line.strip())
        map.append(row)
    file.close()
    return map

def find_current_position(map):
    for row in range(0, len(map)):
        for col in range(0, len(map[0])):
            if map[row][col] in (DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT):
                return (row, col, map[row][col])
    return None, None, None

def move_guard(map, guard_pos_row, guard_pos_col, guard_direction):
    if (guard_direction == DIR_UP):
        if (guard_pos_row - 1) >= 0:
            if map[guard_pos_row - 1][guard_pos_col] not in [OBSTRUCTION_MARKER, LOOP_CHECK_MARKER]:
                map[guard_pos_row][guard_pos_col] = VISITED_MARKER
                map[guard_pos_row - 1][guard_pos_col] = DIR_UP
                guard_pos_row -= 1
            else:
                guard_direction = DIR_RIGHT
                map[guard_pos_row][guard_pos_col] = DIR_RIGHT
        else:
            map[guard_pos_row][guard_pos_col] = VISITED_MARKER
            guard_pos_row = None
    elif (guard_direction == DIR_RIGHT):
        if ((guard_pos_col + 1) < len(map[guard_pos_row])):
            if map[guard_pos_row][guard_pos_col + 1] not in [OBSTRUCTION_MARKER, LOOP_CHECK_MARKER]:
                map[guard_pos_row][guard_pos_col] = VISITED_MARKER
                map[guard_pos_row][guard_pos_col + 1] = DIR_RIGHT
                guard_pos_col += 1
            else:
                guard_direction = DIR_DOWN
                map[guard_pos_row][guard_pos_col] = DIR_DOWN
        else:
            map[guard_pos_row][guard_pos_col] = VISITED_MARKER
            guard_pos_col = None
    elif (guard_direction == DIR_DOWN):
        if ((guard_pos_row + 1) < len(map)):
            if map[guard_pos_row + 1][guard_pos_col] not in [OBSTRUCTION_MARKER, LOOP_CHECK_MARKER]:
                map[guard_pos_row][guard_pos_col] = VISITED_MARKER
                map[guard_pos_row + 1][guard_pos_col] = DIR_DOWN
                guard_pos_row += 1
            else:
                guard_direction = DIR_LEFT
                map[guard_pos_row][guard_pos_col] = DIR_LEFT
        else:
            map[guard_pos_row][guard_pos_col] = VISITED_MARKER
            guard_pos_row = None
    elif (guard_direction == DIR_LEFT):
        if (guard_pos_col - 1) >= 0:
            if map[guard_pos_row][guard_pos_col - 1] not in [OBSTRUCTION_MARKER, LOOP_CHECK_MARKER]:
                map[guard_pos_row][guard_pos_col] = VISITED_MARKER
                map[guard_pos_row][guard_pos_col - 1] = DIR_LEFT
                guard_pos_col -= 1
            else:
                guard_direction = DIR_UP
                map[guard_pos_row][guard_pos_col] = DIR_UP
        else:
            map[guard_pos_row][guard_pos_col] = VISITED_MARKER
            guard_pos_row = None
    return guard_pos_row, guard_pos_col, guard_direction

def print_map(map):
    for row in range(0, len(map)):
        print("".join(c for c in map[row]))
    print()

def count_visited_positions(map):
    count = 0
    for row in map:
        for pos in row:
            if pos == VISITED_MARKER:
                count += 1
    return count


original_map = load_data('aoc_day_06_part_2.dat')
print_map(original_map)

visited_location_map = copy.deepcopy(original_map)
guard_pos_row, guard_pos_col, guard_direction = find_current_position(visited_location_map)
while (guard_pos_row != None and guard_pos_col != None):
    guard_pos_row, guard_pos_col, guard_direction = move_guard(visited_location_map, guard_pos_row, guard_pos_col, guard_direction)

print_map(visited_location_map)
count = count_visited_positions(visited_location_map)
print(count)

count = 0
curr_row = 0
print()
while (curr_row < len(original_map)):
    print("Current Row: %s" % curr_row)
    curr_col = 0
    while curr_col < len(original_map[curr_row]):
        print("Current Column: %s" % curr_col)
        if visited_location_map[curr_row][curr_col] == VISITED_MARKER:
            if original_map[curr_row][curr_col] not in [DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT]:
                current_map = copy.deepcopy(original_map)
                current_map[curr_row][curr_col] = LOOP_CHECK_MARKER
                print_map(current_map)
                previous_positions = []
                guard_pos_row, guard_pos_col, guard_direction = find_current_position(current_map)
                previous_positions.append((guard_pos_row, guard_pos_col, guard_direction))
                while (guard_pos_row != None and guard_pos_col != None):
                    guard_pos_row, guard_pos_col, guard_direction = move_guard(current_map, guard_pos_row, guard_pos_col, guard_direction)
                    if (guard_pos_row, guard_pos_col, guard_direction) in previous_positions:
                        print("Stuck In A Loop")
                        # print_map(current_map)
                        count += 1
                        break
                    previous_positions.append((guard_pos_row, guard_pos_col, guard_direction))
        curr_col += 1
    curr_row += 1


# print_map(original_map)
print(count)
