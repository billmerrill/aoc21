import re
 
# fh = open('ex.txt', 'r')
fh = open('input.txt', 'r')

readings = []
outputs = []

datas = fh.readlines()
for line in datas:
    line_reading = []
    line_output = []
    do_reading = True
    for chonk in re.split(r'\s+', line.strip()):
        if chonk == '|':
            do_reading = False
            continue
        if do_reading:
            line_reading.append(chonk)
        else:
            line_output.append(chonk)
    readings.append(line_reading)
    outputs.append(line_output)

print(readings[0])
print(outputs[0])

# n the output values, how many times do digits 1, 4, 7, or 8 appear?
# 1 len 2, 4 len 4, 7 len 3, 8 len 7

counts = {1:0, 4:0, 7:0, 8:0}
for output in outputs:
    for num in output:
        match len(num):
            case 2:
                counts[1] += 1
            case 3:
                counts[7] += 1
            case 4:
                counts[4] += 1
            case 7:
                counts[8] += 1

print(sum(counts.values()))


