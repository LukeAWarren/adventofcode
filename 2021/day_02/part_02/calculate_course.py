lines = []
with open('course.dat', 'r') as f:
    lines = f.readlines()
    
horizonal_position = 0
depth = 0
aim = 0

for line in lines:
    course_change = line.split(' ')
    command = course_change[0]
    value = int(course_change[1])
    
    if command == 'down':
        aim += value
    if command == 'up':
        aim -= value
    if command == 'forward':
        horizonal_position += value
        depth += aim * value
        
print (f'horizonal_position: {horizonal_position}, depth: {depth}')
print (f'horizonal_position X depth: {horizonal_position * depth}')