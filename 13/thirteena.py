import numpy as np

# fname = '/Users/bill/fun/aoc21/13/ex.txt'
fname = '/Users/bill/fun/aoc21/13/input.txt'

points = []
folds = []
max_x = 0
max_y = 0
reading_points = True
with open(fname, 'r') as fh:
    for i, line in enumerate(fh):
        if line != '\n':
            if reading_points:
                points.append(tuple((int(x) for x in line.strip().split(','))))
            else:
                folds.append(line.strip().split(' ')[2])
        else:
            reading_points = False

page = set()
for point in points:
    # ex y fold
    # if point[1] < 7:
    #     page.add(point)
    # else:
    #     page.add((point[0], 7-(point[1]-7)))

    # input x fold
    if point[0] < 655:
        page.add(point)
    else:
        page.add((655-(point[0]-655), point[1]))

print('visible points: ', len(page))
# 815 is wrong (wrong fold inst)

