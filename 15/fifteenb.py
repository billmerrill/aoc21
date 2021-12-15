import heapq
import math
from os import nice
import numpy as np

# fh = open('/Users/bill/fun/aoc21/15/ex.txt', 'r')
# tile_shape = (10,10)
fh = open('/Users/bill/fun/aoc21/15/input.txt', 'r')
tile_shape = (100,100)

lines = fh.readlines()

tile = np.ndarray(shape=tile_shape, dtype=int)
for i,line in enumerate(lines):
    tile[i] =[int(x) for x in line.strip()]

shape = (tile_shape[0]*5, tile_shape[1]*5)
risks = np.ndarray(shape=shape, dtype=int)

for i in range(5):
    for j in range(5):
        for pt, risk in np.ndenumerate(tile):
            map_pt = (pt[0] + tile_shape[0] * i, pt[1] + tile_shape[1] * j)
            base = tile[pt] + i + j
            steps = math.floor(base/10)
            remainder = base % 10
            risks[map_pt] = remainder + steps
           

dists = np.full(shape, np.inf)
dists[0,0] = 0

with open('/Users/bill/fun/aoc21/15/floor.txt', 'w') as fh:
    for row in risks:
        fh.write(''.join([str(x) for x in row])+'\n')

def get_neighbors(map, coord):
    neighbors = []
    if 0 < coord[0] < map.shape[0]:
        neighbors.append((coord[0]-1, coord[1]))
    if 0 <= coord[0] < map.shape[0]-1:
        neighbors.append((coord[0]+1, coord[1]))
    if 0 < coord[1] < map.shape[1]:
        neighbors.append((coord[0], coord[1]-1))
    if 0 <= coord[1] < map.shape[1]-1:
        neighbors.append((coord[0], coord[1]+1))
    return neighbors

def grid_dijkstra(map, dists):
    pq = [(0, (0,0))]
    while len(pq) > 0:
        curr_dist, curr_coord = heapq.heappop(pq)

        if curr_dist > dists[curr_coord]:
            continue

        for neighbor_coord in get_neighbors(map, curr_coord):
            distance = curr_dist + map[neighbor_coord]

            if distance < dists[neighbor_coord]:
                dists[neighbor_coord] = distance
                heapq.heappush(pq, (distance, neighbor_coord))
            
grid_dijkstra(risks, dists)
print(dists.shape)
print(dists[-1,-1])
