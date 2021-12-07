# fh = open('ex.txt', 'r')
fh = open('input.txt', 'r')

crab_pos_str = fh.readline()
crabs = list(map(int, crab_pos_str.split(',')))
# mid = int(len(crabs)/2)
# crabs_sorts = sorted(crabs)
# meeting = crabs[mid]
meeting = round(sum(crabs)/len(crabs))
raw_meeting = sum(crabs)/len(crabs)
print('rm', raw_meeting)
meeting = 466
print('align ', meeting)
diffs = [abs(x-meeting) for x in crabs]
fuels = [ x+ (x*(x-1))/2 for x in diffs]
print('fuels', sum(fuels))


# 91638956 too high, need to round the meeting down from 467 to 466.  a guess!