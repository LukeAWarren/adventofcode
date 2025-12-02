import os

def mul(x,y):
    return x * y

def load_data(file_name):
    f = open(file_name)
    instructions_string = ""
    for line in f.readlines():
        instructions_string += line.strip()
    instructions = list(instructions_string)
    return instructions

instructions = load_data('aoc_day_03_part_1.dat')

sum = 0

while len(instructions) > 0:
    current_x = ""
    current_y = ""
    # m
    if len(instructions) > 0 and instructions[0] == 'm':
        del instructions[0]

        # u
        if len(instructions) > 0 and instructions[0] == 'u':
            del instructions[0]

            # must be l
            if len(instructions) > 0 and instructions[0] == 'l':
                del instructions[0]

                # must be beginning paren (
                if len(instructions) > 0 and instructions[0] == '(':
                    del instructions[0]
                    # find x
                    if len(instructions) > 0 and instructions[0].isdigit():
                        while (len(instructions) > 0 and instructions[0].isdigit()):
                            current_x += instructions[0]
                            del instructions[0]
                    else:
                        del instructions[0]

                    # find ,
                    if len(instructions) > 0 and instructions[0] == ',':
                        del instructions[0]
                    else:
                        del instructions[0]
                        
                    # find y
                    if len(instructions) > 0 and instructions[0].isdigit():
                        while (len(instructions) > 0 and instructions[0].isdigit()):
                            current_y += instructions[0]
                            del instructions[0]
                    else:
                        del instructions[0]

                    # find closing paren)
                    if len(instructions) > 0 and instructions[0] == ')':
                        sum += mul(int(current_x), int(current_y))
                        del instructions[0]
                    else:
                        del instructions[0]

                else:
                    del instructions[0]
            else:
                del instructions[0]
        else:
            del instructions[0]            
    else:
        del instructions[0]        
               

print(sum)