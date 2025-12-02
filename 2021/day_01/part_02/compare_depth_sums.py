lines = []
with open('depths.dat', 'r') as f:
    lines = f.readlines()

# convert lines in integer values with for loops
depths = []
for line in lines:
    if not line:
        break
    depths.append(int(line))

count_increasing_windows = 0
previous_window = 999999999
for i in range(len(depths) - 2):
    current_window = depths[i] + depths[i+1] + depths[i+2]
    if (current_window > previous_window):
        count_increasing_windows += 1
    previous_window = current_window

print(f'number of increasing windows: {count_increasing_windows}')

# convert lines in integer values with list comprehension
depths = []
depths = [int(depth) for depth in lines]
print(depths)
