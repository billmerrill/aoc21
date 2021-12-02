"""
up down forward
"""
import re

pos_run = 0
pos_depth = 0
pos_aim = 0

course = open('input.txt', 'r').readlines()
for command in course:
    verb, noun, *other = re.split(r'\s+', command)
    if verb == 'up':
        pos_aim -= int(noun)
    elif verb == 'down':
        pos_aim += int(noun)
    elif verb == 'forward':
        pos_run += int(noun)
        pos_depth += int(noun) * pos_aim


print (f"run {pos_run} depth {pos_depth}")
print (pos_run * pos_depth)
    