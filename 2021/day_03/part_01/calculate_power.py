
lines = []
with open('diagnostics.dat') as f:
    lines = f.readlines()

NUMBER_OF_BITS = len(lines[0].strip())
print(f'NUMBER_OF_BITS: {NUMBER_OF_BITS}')

count_ones = [0] * NUMBER_OF_BITS
count_zeros = [0] * NUMBER_OF_BITS

print(count_ones)
print(count_zeros)

for line in lines:
    bits = [int(x) for x in list(line.strip())]    
    #print(bits)
    for i in range(NUMBER_OF_BITS):
        if (bits[i] == 1):
            count_ones[i] += 1
        if (bits[i] == 0):
            count_zeros[i] += 1

#print(count_ones)
#print(count_zeros)

gamma_values = [0] * NUMBER_OF_BITS

for i in range(NUMBER_OF_BITS):
    if (count_ones[i] > count_zeros[i]):
        gamma_values[i] = 1
        
print(gamma_values)

epsilon_values = [0] * NUMBER_OF_BITS

for i in range(NUMBER_OF_BITS):
    if (count_ones[i] < count_zeros[i]):
        epsilon_values[i] = 1
        
print(epsilon_values)


gamma_string = str()
epsilon_string = str()

for i in range(NUMBER_OF_BITS):
    gamma_string += str(gamma_values[i])
    epsilon_string += str(epsilon_values[i])
    
print(gamma_string)
print(epsilon_string)

gamma_value = int(gamma_string, base=2)
epsilon_value = int(epsilon_string, base=2)

print(gamma_value)
print(epsilon_value)

print(f'power consumption = gamma X epsilon : {gamma_value * epsilon_value}')