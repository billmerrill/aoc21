>>> fh = open ('input.txt', 'r')
>>> depths = rh.readlines()


>>> depth_count = 0; prev = 999999

>>> fh.seek(0)
0
>>> for depth in depths:
...     if int(depth) > prev:
...             depth_count += 1
...     prev = int(depth)
...
>>> depth_count
