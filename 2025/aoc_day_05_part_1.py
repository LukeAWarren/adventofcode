import os
from pprint import pprint

FILE = '2025/aoc_day_05.dat'

def load_ingredient_database(file_name):
    fresh_ingredient_ranges = []
    ingredient_list = []

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if '-' in line:
                first_ingredient_id, last_ingredient_id = map(int, line.split('-', 1))
                fresh_ingredient_ranges.append((first_ingredient_id, last_ingredient_id))
            elif line.isdigit():
                ingredient_list.append(int(line))

    return fresh_ingredient_ranges, ingredient_list

fresh_ingredient_ranges, ingredient_list = load_ingredient_database(FILE)

def find_fresh_ingredients(fresh_ingredient_ranges, ingredient_list):
    fresh_ingredients = []
    for ingredient in ingredient_list:
        # print(f'ingredient: {ingredient}')
        for (first_ingredient_id, last_ingredient_id) in fresh_ingredient_ranges:
            # print(f'first_ingredient_id: {first_ingredient_id}, last_ingredient_id: {last_ingredient_id}')
            if first_ingredient_id <= ingredient and last_ingredient_id >= ingredient:
                fresh_ingredients.append(ingredient)
                break
    return fresh_ingredients
pprint(fresh_ingredient_ranges)
pprint(ingredient_list)

fresh_ingredients = find_fresh_ingredients(fresh_ingredient_ranges, ingredient_list)

pprint(fresh_ingredients)
num_fresh_ingredients = len(fresh_ingredients)

print(f'num_fresh_ingredients = {num_fresh_ingredients}')
