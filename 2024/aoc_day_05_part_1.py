import os

rules = []
updates = []
sum = 0
def load_data(file_name, rules, updates):
    f = open(file_name)
    for line in f.readlines():
        if '|' in line:
            # convert rules to types
            first, second = line.strip().split('|')
            rules.append((int(first), int(second)))
        if ',' in line:
            update = [int(page) for page in line.strip().split(',')]
            updates.append(update)

def find_pos(page, update):
    for pos in range(0, len(update)):
        if page == update[pos]:
            return pos
    return None

def check_rules(rules, updates):
    updates_to_remove = []
    for update in updates:
        for rule in rules:
            first, second = rule
            position_of_first_page = find_pos(first, update)
            position_of_second_page = find_pos(second, update)
            if (position_of_first_page != None and position_of_second_page != None):
                if position_of_second_page < position_of_first_page:
                    updates_to_remove.append(update)
                    break
    for update in updates_to_remove:
        updates.remove(update)

def sum_middle_pages(updates):
    sum = 0
    for update in updates:
        mid_pos = (len(update) // 2)
        sum += update[mid_pos]
    return sum

load_data('aoc_day_05_part_1.dat', rules, updates)

check_rules(rules, updates)
sum = sum_middle_pages(updates)

print(sum)
