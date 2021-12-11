from decimal import InvalidContext
import numpy as np
import scipy.ndimage

# if True:
if False:
    fh = open('/Users/bill/fun/aoc21/9/ex.txt', 'r')
    shape = (5,10)
else:
    fh = open('/Users/bill/fun/aoc21/9/input.txt', 'r')
    shape = (100,100)

lines = fh.readlines()

seafloor = np.ndarray(shape=shape, dtype=int)
for i,line in enumerate(lines):
    seafloor[i] =[int(x) for x in line.strip()]

neighbors = np.array(
      [[0, 1, 0],
       [1, 0, 1],
       [0, 1, 0]])
lowpoints = seafloor < scipy.ndimage.minimum_filter(seafloor, footprint=neighbors, mode='constant', cval=999)
low_values = lowpoints * np.ones(shape=lowpoints.shape) + seafloor*lowpoints
print('low point count', (lowpoints * np.ones(shape=lowpoints.shape, dtype=int)).sum())

basin_origins = []
for pt, value in np.ndenumerate(lowpoints):
    if value:
        basin_origins.append(pt)

visited = set()
basins = []
for pt, value in np.ndenumerate(seafloor):
    if pt in visited or value == 9:
        continue
    basin_size = 0
    potentials = set([pt])
    # visited.add(pt)
    while potentials:
        p = potentials.pop() 
        if p in visited:
            continue
        basin_size += 1
        visited.add(p)

        if p[0] > 0 and seafloor[p[0]-1,p[1]] != 9:
            potentials.add((p[0]-1, p[1]))
        if p[0] < seafloor.shape[0]-1 and seafloor[p[0]+1, p[1]] != 9:
            potentials.add((p[0]+1, p[1]))

        if p[1] > 0 and seafloor[p[0],p[1]-1] != 9:
            potentials.add((p[0], p[1]-1))
        if p[1] < seafloor.shape[1]-1 and seafloor[p[0], p[1]+1] != 9:
            potentials.add((p[0], p[1]+1))

    basins.append(basin_size)

print(basins)
basins = sorted(basins, reverse=True)
print(basins[0] * basins[1] * basins[2])






