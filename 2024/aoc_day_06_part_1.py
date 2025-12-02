import os

map = []
count = 0
DIR_UP = '^'
DIR_RIGHT = '>'
DIR_DOWN = 'v'
DIR_LEFT = '<'
VISITED_MARKER = 'X'
OBSTRUCTION_MARKER = '#'

def load_data(file_name, map):
    file = open(file_name)
    for line in file.readlines():
        row = list(line.strip())
        map.append(row)
    file.close()


def find_current_position(map):
    for row in range(0, len(map)):
        for col in range(0, len(map[0])):
            if map[row][col] in (DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT):
                return (row, col, map[row][col])
    return None, None, None

def move_guard(map, guard_pos_row, guard_pos_col, guard_direction):
    if (guard_direction == DIR_UP):
        if (guard_pos_row - 1) >= 0:
            if map[guard_pos_row - 1][guard_pos_col] != OBSTRUCTION_MARKER:
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
            if map[guard_pos_row][guard_pos_col + 1] != OBSTRUCTION_MARKER:
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
            if map[guard_pos_row + 1][guard_pos_col] != OBSTRUCTION_MARKER:
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
            if map[guard_pos_row][guard_pos_col - 1] != OBSTRUCTION_MARKER:
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


load_data('aoc_day_06_part_1.dat', map)
print_map(map)
guard_pos_row, guard_pos_col, guard_direction = find_current_position(map)
while (guard_pos_row != None and guard_pos_col != None):
    guard_pos_row, guard_pos_col, guard_direction = move_guard(map, guard_pos_row, guard_pos_col, guard_direction)
    # print_map(map)

print_map(map)
count = count_visited_positions(map)
print(count)
