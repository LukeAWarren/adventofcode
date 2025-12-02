from pymysql import NUMBER


lines = []
with open('diagnostics.dat', 'r') as f:
    lines = f.readlines()
    
NUMBER_OF_BITS = len(lines[0].strip())
print(lines)
print(f'NUMBER_OF_BITS: {NUMBER_OF_BITS}')

life_support_data = []
for line in lines:
    life_support_data.append([int(x) for x in list(line.strip())])

print(life_support_data)

# find the most common bit for the position
position = 0

def filter_data_by_oxygen_criteria(position, data):
    count_ones = 0
    count_zeros = 0
    
    for row in data:
        if(row[position] == 1):
            count_ones += 1
        if(row[position] == 0):
            count_zeros += 1
    
    filtered_data = []
    # now filter the data based on which number was most common
    if count_ones >= count_zeros:        
        for row in data:
            if row[position] == 1:
                filtered_data.append(row)
    if count_zeros > count_ones:
        for row in data:
            if row[position] == 0:
                filtered_data.append(row)
    return filtered_data

def filter_data_by_co2_scrubber_criteria(position, data):
    count_ones = 0
    count_zeros = 0
    
    for row in data:
        if(row[position] == 1):
            count_ones += 1
        if(row[position] == 0):
            count_zeros += 1
    
    print(f'count_ones: {count_ones}')
    print(f'count_zeros: {count_zeros}')
    filtered_data = []
    # now filter the data based on which number was most common
    if count_ones < count_zeros:
        for row in data:
            if row[position] == 1:
                filtered_data.append(row)
    if count_zeros <= count_ones:
        for row in data:
            if row[position] == 0:
                filtered_data.append(row)
    return filtered_data

filtered_oxygen_data = life_support_data
for position in range(NUMBER_OF_BITS):
    print(f'position: {position}')
    filtered_oxygen_data = filter_data_by_oxygen_criteria(position, filtered_oxygen_data)
    if (len(filtered_oxygen_data) == 1):
        break

filtered_co2_data = life_support_data
for position in range(NUMBER_OF_BITS):
    print(f'position: {position}')
    filtered_co2_data = filter_data_by_co2_scrubber_criteria(position, filtered_co2_data)
    if len(filtered_co2_data) == 1:
        break

print(filtered_oxygen_data)
print(filtered_co2_data)

oxygen_string = str()
co2_string = str()

for i in range(NUMBER_OF_BITS):
    oxygen_string += str(filtered_oxygen_data[0][i])
    co2_string += str(filtered_co2_data[0][i])

print(f'oxygen_string: {oxygen_string}')
print(f'co2_string: {co2_string}')

oxygen_value = int(oxygen_string, base=2)
co2_value = int(co2_string, base=2)

print(f'oxygen_value: {oxygen_value}')
print(f'co2_value: {co2_value}')

print(f'life support rating = oxygen X co2: {oxygen_value * co2_value}')
