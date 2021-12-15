import heapq
from os import nice
import numpy as np

# fh = open('/Users/bill/fun/aoc21/15/ex.txt', 'r')
# shape = (10,10)
fh = open('/Users/bill/fun/aoc21/15/input.txt', 'r')
shape = (100,100)

lines = fh.readlines()

risks = np.ndarray(shape=shape, dtype=int)
for i,line in enumerate(lines):
    risks[i] =[int(x) for x in line.strip()]

dists = np.full(shape, np.inf)
dists[0,0] = 0

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

def calculate_distances(map, dists):
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
            
calculate_distances(risks, dists)
print(dists[-1,-1])

