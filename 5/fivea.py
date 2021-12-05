import numpy as np
import re

def draw_diag(seafloor, start, end):
    if start[1] < end[1]:
        y_inc = 1
    else:
        y_inc = -1

    y = start[1]
    print('starting', y, start[0], end[0])
    for x in range(start[0], end[0]):
        print('\t', x, y)
        seafloor[x][y] += 1
        y += y_inc



seafloor = np.zeros(shape=(1000,1000), dtype=int)
vents = open('input.txt', 'r').readlines()

# seafloor = np.zeros(shape=(10,10), dtype=int)
# vents = open('example.txt', 'r').readlines()

pattern = r'(\S+),(\S+) -> (\S+),(\S+)'
counts =[0,0,0]
for vent in vents:
    r = re.search(pattern, vent)
    points = [int(x) for x in r.groups()]
    if points[0] == points[2]:
        # print('vert', points)
        start = points[1]
        end = points[3]
        if points[3] < points[1]:
            start = points[3]
            end = points[1]
        seafloor[points[0], start:end+1] += 1
        counts[0] += 1
    elif points[1] == points[3]:
        # print('slide', points)
        start = points[0]
        end = points[2]
        if points[2] < points[0]:
            start = points[2]
            end = points[0]
        seafloor[start:end+1, points[1]] += 1
        counts[1] += 1
    elif points[0] < points[2]:
        print('zero first')
        print(points)
        start = (points[0], points[1])
        end = (points[2]+1, points[3])
        draw_diag(seafloor, start, end)
    else:
        print(points)
        end = (points[0]+1, points[1])
        start = (points[2], points[3])
        draw_diag(seafloor, start, end)

print(seafloor)
# >>> len(y[y[:]>0])
x = seafloor.flatten()
filter = x[x[:]>1]
print(filter)
print(len(filter))
# not 10106 too high
# not 21552 too low

print(counts)
print(sum(counts))
