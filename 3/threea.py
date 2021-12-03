"""
1010 1111 1001
"""
total_readings = 0
read_len = 0
accumulator = []
readings = open('input.txt', 'r').readlines()
for reading in readings:
    if read_len == 0:
        read_len = len(reading) - 1
        print(reading, read_len)
        accumulator = [0] * read_len


    total_readings += 1
    for i, bit in enumerate(reading):
        if bit.isdecimal():
            accumulator[i] += int(bit)

print(accumulator)
gamma_bits = [0] * read_len
epsilon_bits = [0] * read_len

half_readings = total_readings / 2

for i, bit in enumerate(accumulator):
    print(i, bit)
    if accumulator[i] > half_readings:
        gamma_bits[i] = '1'
        epsilon_bits[i] = '0'
    else:
        gamma_bits[i] = '0'
        epsilon_bits[i] = '1'

gamma = int(''.join(gamma_bits),2)
epsilon = int(''.join(epsilon_bits),2)
print(gamma, epsilon, gamma * epsilon)


print(gamma_bits)
print(epsilon_bits)

