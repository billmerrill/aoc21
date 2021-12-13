import numpy as np

# fname = '/Users/bill/fun/aoc21/13/ex.txt'
fname = '/Users/bill/fun/aoc21/13/input.txt'

points = []
folds = []
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

page = set(points)
new_page = set()
for fold in folds:
    fold_axis, fold_line = fold.split('=')
    fold_line = int(fold_line)
    for point in page:
        if fold_axis == 'y':
            if point[1] < fold_line:
                new_page.add(point)
            else:
                new_page.add((point[0], fold_line-(point[1]-fold_line)))
        if fold_axis == 'x':
            if point[0] < fold_line:
                new_page.add(point)
            else:
                new_page.add((fold_line-(point[0]-fold_line), point[1]))
    page = new_page
    new_page = set()

print('visible points: ', len(page))
# 815 is wrong (wrong fold inst)
print(page)

max = [0,0]
for point in page:
    if point[0] > max[0]:
        max[0] = point[0]
    if point[1] > max[1]:
        max[1] = point[1]
max = (max[0]+1, max[1]+1)
max = (max[1], max[0])

display_page = np.full(max, ' ', dtype=str)
for point in page:
    display_page[point[1], point[0]] = '*'

with open('/Users/bill/fun/aoc21/13/bottle.txt', 'w') as fh:
    for row in display_page:
        fh.write(''.join(row) + '\n')


# nope UCZRAZU (was a typo!)
# UCLZRAZU