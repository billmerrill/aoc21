import numpy as np
import scipy.ndimage


# fh = open('ex.txt', 'r')
# shape = (5,10)
fh = open('input.txt', 'r')
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
# >>> ans * np.ones(shape=ans.shape) + seafloor*ans
low_values = lowpoints * np.ones(shape=lowpoints.shape) + seafloor*lowpoints
print(low_values.sum())

