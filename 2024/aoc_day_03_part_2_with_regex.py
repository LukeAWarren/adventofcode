import os
import re

def mul(x,y):
    return x * y

def load_data(file_name):
    f = open(file_name)
    instructions = ""
    for line in f.readlines():
        instructions += line.strip()    
    return instructions

instructions = load_data('aoc_day_03_part_2.dat')

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, instructions)

res = 0
flag = True
for match in matches:
    if match == "do()":
        flag = True
    elif match == "don't()":
        flag = False
    else:
        if flag:
            args = match[4:-1]
            x, y = map(int, args.split(","))
            res += x * y

print(res)