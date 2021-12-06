fh = open('input.txt', 'r')
target = 80
# fh = open('ex.txt', 'r')
# target = 18

fish_str = fh.readline()
the_deep = fish_str.split(',')
the_deep = [int(x) for x in the_deep]
day = 0

def day_tick(the_deep):
    new_fish = []
    for i, fish in enumerate(the_deep):
        if fish == 0:
            new_fish.append(8)
            the_deep[i] = 6
        else:
            the_deep[i] -= 1

    the_deep.extend(new_fish)

def show_state(the_deep, day):
    print(f'day {day}:', the_deep)

# show_state(the_deep, 0)
for i in range(target):
    day += 1
    day_tick(the_deep)
    # show_state(the_deep, day)
print(len(the_deep))

