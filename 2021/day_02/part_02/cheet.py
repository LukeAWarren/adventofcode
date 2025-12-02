import os

VERTICAL_COMMAND = {"up": -1, "down": 1}


def get_instructions(l):
    return [tuple(_l.split()) for _l in l]


def solution2(l):
    x = 0
    aim = 0
    depth = 0
    instuctions = get_instructions(l)
    for command, value in instuctions:
        if command == "forward":
            x += int(value)
            depth += int(value) * aim
        else:
            aim += VERTICAL_COMMAND[command] * int(value)
    print(f'horitontal_position: {x}, depth: {depth}')
    return x * depth


if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()

    print(solution2(data))