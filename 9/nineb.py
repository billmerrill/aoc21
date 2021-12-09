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
        top_neighbor = (pt[0]-1, pt[1])
        if top_neighbor[0] < 0 ||
            canvas[top_neighbor] == 9:
            top = False

        #bottom
        bottom_neighbor = (pt[0]+1, pt[1])
        #left
        left_neighbor = (pt[0], pt[1]-1)
        #right
        right_neighbor = (pt[0], pt[1]+1)
        



sizes = []
for basin_origin in basin_origins:
    sizes.append(compute_size(seafloor, basin_origin))





