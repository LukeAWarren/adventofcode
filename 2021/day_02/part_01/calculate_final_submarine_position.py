course_data = []
with open('course.dat', 'r') as f:
    course_data = f.readlines()

position = 0
depth = 0
direction = str()
change = int()

for positon_change in course_data:
    course_change = positon_change.split(' ')
    direction = str(course_change[0])
    change = int(course_change[1])
    if (direction == 'forward'):
        position += change
    if (direction == 'up'):
        depth -= change
    if (direction == 'down'):
        depth += change
        
print(f'position: {position}, depth: {depth}')
print(f'position x depth = {position * depth}')