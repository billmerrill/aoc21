from scipy.signal import convolve
from itertools import pairwise

fh = open ('input.txt', 'r')
depths = fh.readlines()

kernel = [1,1,1]
depths = [int(x) for x in depths]
convolved = convolve(depths, kernel, mode='valid')

deeper = 0
for a,b in pairwise(convolved):
    if b > a:
        deeper += 1

print(deeper)
