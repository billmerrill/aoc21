# fh = open('ex.txt', 'r')
fh = open('input.txt', 'r')

crab_pos_str = fh.readline()
crabs = list(map(int, crab_pos_str.split(',')))
mid = int(len(crabs)/2)
crabs_sorts = sorted(crabs)
meeting = crabs[mid]
print('aling ', meeting)
print('fuel ', sum([abs(meeting-x) for x in crabs]))

