import numpy as np

read_len = 0
total_readings = 0
readings = []
readings_file = open('input.txt', 'r').readlines()

for reading in readings_file:
    if read_len == 0:
        read_len = len(reading) - 1
        print(reading, read_len)
    total_readings += 1
    accumulator = [0] * read_len
    for i, bit in enumerate(reading):
        if bit.isdecimal():
            accumulator[i] = int(bit)
    readings.append(accumulator)

half_readings = total_readings / 2
mat = np.array(readings)

oxy = mat.copy()
col = 0
while len(oxy) > 1:
    col_sum = np.sum(oxy[:, col])
    if col_sum >= (len(oxy)/2):
        # keep 1s
        oxy = oxy[oxy[:, col]==1,:]
    else:
        # keep 0s
        oxy = oxy[oxy[:, col]==0,:]
    col += 1

print('oxy', oxy)

co2 = mat.copy()
col = 0
while len(co2) > 1:
    col_sum = np.sum(co2[:, col])
    if col_sum < (len(co2)/2):
        # keep 1s
        co2 = co2[co2[:, col]==1,:]
    else:
        # keep 0s
        co2 = co2[co2[:, col]==0,:]
    col += 1

print('co2', co2)
oxy_reading = int(''.join(map(str, oxy[0])), 2)
co2_reading = int(''.join(map(str, co2[0])), 2)
print(oxy_reading, co2_reading, oxy_reading*co2_reading)