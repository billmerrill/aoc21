from decimal import InvalidContext
import numpy as np
import scipy.ndimage

if True:
# if False:
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

def sample_seafloor(seafloor, pt, default=9):
    sample = np.ndarray(shape=(3,3), dtype=int)
    sample.fill(default)
    for i in range (-1,2):
        if 0 <= pt[0] + i < seafloor.shape[0]:
            for j in range (-1,2):
                if 0 <= pt[1]+j < seafloor.shape[1]:
                    sample[i+1, j+1] = seafloor[pt[0]+i, pt[1]+j]
    return sample

def write_seafloor(seafloor, name):
    with open(name, 'w') as fh:
        for row in seafloor:
            rowstr = ''.join(list(map(str,row)))
            fh.write(rowstr + '\n')

write_seafloor(seafloor, 'bob.txt')

def compute_size(seafloor_in, origin):
    seafloor = seafloor_in.copy()
    top = np.array([[0,1,0], [1,0,1], [0,0,0]])
    bottom = np.array([[0,0,0], [1,0,1], [0,1,0]])
    left = np.array([[0,1,0], [1,0,0], [0,1,0]])
    right = np.array([[0,1,0], [0,0,1], [0,1,0]])
    neighbor_masks = [top, bottom, left, right]

    top_pt_xform = np.array((-1,0))
    bottom_pt_xform = np.array((1,0))
    left_pt_xform = np.array((0, -1))
    right_pt_xform = np.array((0, 1))
    neighbor_xforms = [top_pt_xform, bottom_pt_xform, left_pt_xform, right_pt_xform]

    basin = set([origin])
    # mark the map so we don't confuse checks with lower parts of the basin
    seafloor[tuple(origin)] = 9

    invest_neighbors = set([origin])

    while invest_neighbors:
        # members of invest neighbors are basin
        # let's check to see if their neighbors are, and add them to basin, so we can check their neighbors
        iteration_invest = set()
        pt = np.array(invest_neighbors.pop())
        if seafloor[tuple(pt)] == 9:
            continue
        neighbors = pt + neighbor_xforms
        for i, neighbor in enumerate(neighbors):
            if tuple(neighbor) not in basin:
                neighbor_sample = sample_seafloor(seafloor, neighbor)
                heights = neighbor_sample[1,1] < (neighbor_sample * neighbor_masks[i])
                # all the neighbors's heights are greater than neighbor 
                # 3 trues on the left make 3, mask also sums to 3
                if ((0 <= neighbor[0] < seafloor.shape[0]) and 
                    (0 <= neighbor[1] < seafloor.shape[1]) and
                    (heights * neighbor_masks[i]).sum() == neighbor_masks[i].sum()):
                    basin.add(tuple(neighbor))
                    invest_neighbors.add(tuple(neighbor))
                    # iteration_invest.add(tuple(neighbor))
                    # mark the map so we don't confuse checks with lower parts of the basin
                    seafloor[tuple(neighbor)] = 9
        # invest_neighbors = invest_neighbors.union(iteration_invest)

    # print(seafloor) 
    # write_seafloor(seafloor, 'bob.txt')
    return basin
        
sizes = []
for basin_origin in basin_origins:
    a_basin = compute_size(seafloor, basin_origin)
    if len(a_basin) > 90:
        print('big origin',  basin_origin)
    sizes.append(len(a_basin))

# sizes = [compute_size(seafloor, (87,5))]

print(sizes)
sizes = sorted(sizes, reverse=True)
print('num sizes', len(sizes))
print(sizes)
print(sizes[0] * sizes[1] * sizes[2])

# 626899 is too low
# may be 949905

# >>> top
# array([[0, 1, 0],
#        [1, 0, 1],
#        [0, 0, 0]])
# >>> k = seafloor[1:4, 1:4]
# >>> k
# array([[9, 8, 7],
#        [8, 5, 6],
#        [7, 6, 7]])
# >>> k * top
# array([[0, 8, 0],
#        [8, 0, 6],
#        [0, 0, 0]])
# >>> k[2,2]
# 7
# >>> k[1,1]
# 5
# >>> k[1,1] < (k*top)
# array([[False,  True, False],
#        [ True, False,  True],
#        [False, False, False]])
# >>> kans = _
# >>> kans * top
# array([[0, 1, 0],
#        [1, 0, 1],
#        [0, 0, 0]])
# >>> sum(kans * top)
# array([1, 1, 1])
# >>> (kans * top).sum()
# 3
# >>> (kans * top).sum() == top.sum()
# True
# >>> k = seafloor[0:3, 0:3]
# >>> kans = k[1,1] < (k*top)
# >>> kans
# array([[False, False, False],
#        [False, False, False],
#        [False, False, False]])
# >>> k
# array([[2, 1, 9],
#        [3, 9, 8],
#        [9, 8, 5]])
# >>> (kans * top).sum() == top.sum()
# False
# >>> seafloor
# array([[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
#        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
#        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
#        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
#        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]])