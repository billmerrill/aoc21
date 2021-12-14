from collections import Counter, defaultdict
import datetime
from itertools import pairwise
from os import readlink

import numpy as np


fname = '/Users/bill/fun/aoc21/14/ex.txt'
# fname = '/Users/bill/fun/aoc21/14/input.txt'

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

# Template:     NNCB
# After step 1: NCNBCHB
# After step 2: NBCCNBBBCBHCB

counts = defaultdict(int)
def walk_soup(counts):
    def count_chars(a, b, steps, counts):
        counts[recipe[a+b]] += 1
        if steps == 1:
            return 
        count_chars(a, recipe[a+b], steps-1, counts)
        count_chars(recipe[a+b], b, steps-1, counts)

    for a,b in pairwise(soup):
        print(a,b)
        print(datetime.datetime.now())
        counts[a] += 1
        count_chars(a,b,steps,counts)
    
    counts[soup[-1]] += 1
        

print('start ', soup)
print(datetime.datetime.now())
walk_soup(counts)
print(counts)
counter = Counter(counts)
histo = counter.most_common()
print('histo')
print(histo[0][1] - histo[-1][1])
