import os

reports = []
INCREASING = 1
NO_CHANGE = 0
DECREASING = -1

def load_report(file_name, reports):
    file = open(file_name)
    for line in file.readlines():
        levels = [int(x) for x in line.split()]
        reports.append(levels)
    file.close()

def check_direction(previous_level, current_level):
    if (previous_level - current_level) == 0:
        return NO_CHANGE
    if (previous_level - current_level) > 0:
        return DECREASING
    if (previous_level - current_level) < 0:
        return INCREASING

def check_level_increase(report):
    previous_level = None
    previous_direction = None
    for current_level in report:
        if previous_level != None:
            if abs(previous_level - current_level) > 3:
                return False
            current_direction = check_direction(previous_level, current_level)
            if previous_direction != None:
                # check that the levels are consistently changing
                if (current_direction == NO_CHANGE):
                    return False
                if (previous_direction != current_direction):
                    return False
            previous_direction = current_direction
        previous_level = current_level
    return True

def check_reports(reports):
    count = 0
    for report in reports:
        if (check_level_increase(report)):
            count += 1
    return count

load_report('aoc_day_02_part_1.dat', reports)
count = check_reports(reports)
print(count)