
fh = open('input.txt', 'r')
target =256 
# fh = open('ex.txt', 'r')
# target = 18 

fish_str = fh.readline()
the_deep = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

fish_str = fish_str.split(',')
fishes = [int(x) for x in fish_str]
print(fishes)
for fish in fishes:
    the_deep[fish] += 1
day = 0

print('day 0', the_deep)
for i in range(target):
    day += 1
    new_fish = the_deep[0]
    for j in range(0,8):
        the_deep[j] = the_deep[j+1]
    the_deep[6] += new_fish
    the_deep[8] = new_fish
    print(the_deep)
    print('sum', sum(the_deep.values()))



