import os
import itertools

def load_data(file_name):
    equations = {}
    file = open(file_name)
    for line in file.readlines():
        (result_string, constants_string) = line.strip().split(':')
        result = int(result_string)
        constants = [int(x) for x in constants_string.lstrip().split(' ')]
        equations[result] = constants
    file.close()
    return equations

def get_operator_sequences(operators, constants):
    number_of_possible_operators = len(constants) - 1
    operator_sequences = []
    for sequence in itertools.product(operators, repeat=number_of_possible_operators):
        operator_sequences.append(list(sequence))
    return operator_sequences

def operator_on_constants(first, second, operator):
    if operator == '+':
        return first + second
    elif operator == '*':
        return first * second
    elif operator == '||':
        return int(str(first) + str(second))
    else:
        raise("INVALID OPERATOR: %s" % operator)

def test_equation(result, constants):
    num_constants = len(constants)
    operator_sequences = get_operator_sequences(['+', '*', '||'], constants)
    for operator_sequence in operator_sequences:
        aggregator = constants[0]
        for constant_pos in range(0, len(constants) - 1):
            aggregator = operator_on_constants(aggregator, constants[constant_pos + 1], operator_sequence[constant_pos])
        if aggregator == result:
            return result
    return 0

equations = load_data('aoc_day_07_part_2.dat')

sum_of_test_values = 0
for result in equations.keys():
    print("testing: %s with %s", result, equations[result])
    sum_of_test_values += test_equation(result, equations[result])

print(sum_of_test_values)