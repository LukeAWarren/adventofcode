import os
from pprint import pprint

FILE = '2025/aoc_day_06_temp.dat'

def load_math_problem(file_name):
    operands = []
    operators = []

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if parts[0].isdigit():
                operands.append(list(map(int, parts)))
            else:
                operators = parts

    return operands, operators

def multiply(operands, operator):
    total = 1
    for i in range(len(operands)):
        total = total * operands[i - 1]
    return total

def add(operands, operator):
    total = 0
    for i in range(len(operands)):
        total = total + operands[i - 1]
    return total

def do_math(operands, operators):
    grand_total = 0
    row_count = len(operands)
    col_count = len(operands[0]) if operands else 0

    for col_index in range(col_count - 1, 0, -1):
        column_values = []
        for row_index in range(row_count):
            column_values.append(operands[row_index][col_index])

        operator = operators[col_index]
        if operator == '*':
            grand_total += multiply(column_values, operator)
        elif operator == '+':
            grand_total += add(column_values, operator)
    return grand_total

operands, operators = load_math_problem(FILE)
print('operands')
pprint(operands)
print('operators')
pprint(operators)

grand_total = do_math(operands, operators)

print(f'grand_total: {grand_total}')
