fh = open ('input.txt', 'r')
depths = fh.readlines()

depth_count = 0; prev = 999999
for depth in depths:
    if int(depth) > prev:
            depth_count += 1
    prev = int(depth)

print(depth_count)
