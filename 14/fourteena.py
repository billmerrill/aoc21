from collections import Counter
from itertools import pairwise

import numpy as np


fname = '/Users/bill/fun/aoc21/14/ex.txt'
fname = '/Users/bill/fun/aoc21/14/input.txt'

start_sub = ''
insertions = None
recipe = {}
with open(fname, 'r') as fh:
    start_sub = fh.readline().strip()
    space = fh.readline()
    for i, line in enumerate(fh):
        parts =  line.strip().split(' -> ')
        recipe[parts[0]] = parts[1]
        if insertions is None:
            insertions = np.array([[parts[0], parts[1]]])
        else:
            insertions = np.append(insertions,[ [parts[0], parts[1] ] ], axis=0)

steps = 40
soup = start_sub
new_soup = ''
for step in range(steps):
    for a,b in pairwise(soup):
        if a+b in recipe:
            new_soup += a+recipe[a+b]
        else:
            new_soup += a 
    new_soup += b
    
    soup = new_soup
    new_soup = ''
    print(step, len(soup))

counter = Counter(soup)
histo = counter.most_common()
print(histo[0][1] - histo[-1][1])
# too high 52299