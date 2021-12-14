from collections import Counter, defaultdict
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

steps = 10
soup = start_sub
new_soup = ''

pairs = defaultdict(int)
remainder = defaultdict(int)
for a,b in pairwise(soup):
    pairs[a+b] += 1

print('startpairs')
print(pairs)
# Template:     NNCB
# After step 1: NCNBCHB
# After step 2: NBCCNBBBCBHCB

for step in range(steps):
    new_pairs = defaultdict(int)
    past_last = None
    for pair in pairs:
        if pair in recipe:
            left_pair = pair[0] + recipe[pair]
            new_pairs[left_pair] += 1
            new_pairs[pair] -= 1
            if not (past_last is None):
                new_pairs[past_last+pair[0]] += 1
            past_last = recipe[pair]
    # last pair
    remainder[past_last] += 1
    for pair in new_pairs:
        pairs[pair] += new_pairs[pair]

    print(step)
    print(pairs)
    print(remainder)

print("------------------")

single_counts = defaultdict(int)
for pair in pairs:
    single_counts[pair[0]] += pairs[pair]
for rr in remainder:
    single_counts[rr] += 1
# single_counts[pair[1]] += 1
    # single_counts[pair[1]] += pairs[pair]

counter = Counter(single_counts)
print(counter)
histo = counter.most_common()

# print(pairs)
# print(single_counts)
print(histo[0], histo[-1])
print(histo[0][1] - histo[-1][1])

# counter = Counter(soup)