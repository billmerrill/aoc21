import numpy as np
import scipy.ndimage


fh = open('ex.txt', 'r')
shape = (5,10)
# fh = open('input.txt', 'r')
# shape = (100,100)

lines = fh.readlines()

seafloor = np.ndarray(shape=shape, dtype=int)
for i,line in enumerate(lines):
    seafloor[i] =[int(x) for x in line.strip()]

neighbors = np.array(
      [[0, 1, 0],
       [1, 0, 1],
       [0, 1, 0]])
lowpoints = seafloor < scipy.ndimage.minimum_filter(seafloor, footprint=neighbors, mode='constant', cval=999)
# >>> ans * np.ones(shape=ans.shape) + seafloor*ans
low_values = lowpoints * np.ones(shape=lowpoints.shape) + seafloor*lowpoints

basin_origins = []
for i,x in enumerate(lowpoints):
    if x:
        basin_origins.append(i)

def is_basin(base, neighbor):
    
def 

def compute_size(seafloor, origin):
    points = [origin]
    canvas = seafloor.copy()
    for pt in points:
        top = np.array([[0,1,0], [1,0,1], [0,0,0]])
        bottom = np.array([[0,0,0], [1,0,1], [0,1,0]])
        left = np.array([[0,1,0], [1,0,0], [0,1,0]])
        right = np.array([[0,1,0], [0,0,1], [0,1,0]])
        #top
        top_neighbor[0] < 0 ||

        #bottom
        bottom_neighbor = (pt[0]+1, pt[1])
        #left
        left_neighbor = (pt[0], pt[1]-1)
        #right
        right_neighbor = (pt[0], pt[1]+1)
        



sizes = []
for basin_origin in basin_origins:
    sizes.append(compute_size(seafloor, basin_origin))





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