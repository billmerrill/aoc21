import numpy as np

# fh = open('/Users/bill/fun/aoc21/11/ex.txt', 'r')
# shape = (10,10)
fh = open('/Users/bill/fun/aoc21/11/input.txt', 'r')
shape = (10,10)

lines = fh.readlines()

octos = np.ndarray(shape=shape, dtype=int)
for i,line in enumerate(lines):
    octos[i] =[int(x) for x in line.strip()]

print(octos)
curr_step = 0
flashes = 0

neighbors = [
    np.array((-1, -1)),
    np.array((-1, 0)),
    np.array((-1, 1)),
    np.array((0, -1)),
    np.array((0, 1)),
    np.array((1, -1)),
    np.array((1, 0)),
    np.array((1, 1))
]

def incr_neighbors(octos, pt):
    pt = np.array(pt)
    for neighbor in neighbors:
        cur = pt+neighbor
        if 0 <= cur[0] < octos.shape[0] and 0 <= cur[1] < octos.shape[1]:
            octos[tuple(pt+neighbor)] += 1

def trigger_flash(octos):
    global flashes
    for pt, energy in np.ndenumerate(octos):
        if energy > 9:
            incr_neighbors(octos, pt)
            octos[pt] = -50
            flashes += 1

def run_step(octos):
    octos += 1
    flashers = np.where(octos > 9)
    while len(flashers[0]) > 0:
        trigger_flash(octos)
        flashers = np.where(octos > 9)

    step_flashes = 0
    for pt, energy in np.ndenumerate(octos):
        if energy < 0:
            step_flashes += 1
            octos[pt] = 0
    
    return step_flashes == octos.size

print(octos)
for i in range(10000):
    print('step ', i)
    if run_step(octos):
        print('all flashed')
        exit()
# print(flashes)

# too low 1656