import os

movements = []

def load_movements(file_name, movements):
    file = open(file_name)
    for line in file.readlines():
        movements.append(line.strip())
    file.close()

load_movements('2025/aoc_day_01.dat', movements)

def move_left(current_location, distance):
    if distance > 100:
        distance = distance % 100
    temp = current_location - distance
    # print(temp)
    if (temp < 0):
        temp = 100 - abs(temp)
    return temp

def move_right(current_location, distance):
    if distance > 100:
        distance = distance % 100
    temp = current_location + distance
    if (temp > 100):
        temp = temp - 100
    if (temp == 100):
        temp = 0
    return temp

current_location = 50

number_of_zeros = 0

for movement in movements:
    direction = movement[0]
    distance = movement[1:]
    print(f'current_location = {current_location}')
    print(f'movement = {movement}, direction = {direction}, distance = {distance}')
    if direction == 'L':
        current_distance = int(distance)
        while current_distance >= 100:
            number_of_zeros = number_of_zeros + 1
            current_distance = current_distance - 100
        if current_location - current_distance < 0 and current_location > 0:
            number_of_zeros = number_of_zeros + 1
        current_location = move_left(current_location, current_distance)
    elif direction == 'R':
        current_distance = int(distance)
        while current_distance >= 100:
            number_of_zeros = number_of_zeros + 1
            current_distance = current_distance - 100
        if current_location + current_distance > 100:
            number_of_zeros = number_of_zeros + 1
        current_location = move_right(current_location, current_distance)

    if current_location == 0:
        number_of_zeros = number_of_zeros + 1
    print(f'new location: {current_location}')

print(f'number_of_zeros: {number_of_zeros}')
