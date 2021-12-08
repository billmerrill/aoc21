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
            line_reading.append(''.join(sorted(chonk)))
        else:
            line_output.append(''.join(sorted(chonk)))
    readings.append(line_reading)
    outputs.append(line_output)


def analyze_line(num):
    chars = {}
    chonks = []
    chonks.extend(readings[num])
    chonks.extend(outputs[num])
    # print(chonks)
    for chonk in chonks:
        if len(chars) == 4:
            break
        match len(chonk):
            case 2:
                chars[1] = chonk
            case 3:
                chars[7] = chonk
            case 4:
                chars[4] = chonk
            case 7:
                chars[8] = chonk
# 1 2 3 4 5 6 7 8 9 0
# 2 5 5 4 5 6 3 7 6 6
    top = set(chars[7]) - set(chars[1])
    # 9 = len 6 and both 1
    #   9 - 1 = len 4
    #   9 - 4 = len 2
    #   9 - 7 = len 3
    # 6 = len 6 and half 1
    #   6 - 1 = len 5
    #   6 - 2 = len 3
    #   6 - 7 = len 4
    # 0 = len 6
    #   0 - 1 = len 4
    #   0 - 4 = len 3
    #   0 - 7 = len 3
    for chonk in chonks:
        if (len(chars) == 7):
            break
        if len(chonk) == 6:
            m_one = len(set(chonk) - set(chars[1]))
            m_four = len(set(chonk) - set(chars[4]))
            m_sev = len(set(chonk) - set(chars[7]))
            sig = (m_one, m_four, m_sev)
            match sig:
                case (4,2,3):
                    chars[9] = chonk
                case (5,3,4):
                    chars[6] = chonk
                case (4,3,3):
                    chars[0] = chonk

    for chonk in chonks:
        if len(chonk) == 5:
            nine_min = len(set(chars[9]) - set(chonk))
            six_min = len(set(chars[6]) - set(chonk))
            m_one = len(set(chonk) - set(chars[1]))
            if nine_min == 1 and six_min == 1:
                chars[5] = chonk
            elif nine_min == 2 and six_min == 2:
                chars[2] = chonk
            elif nine_min == 1 and six_min == 2 and m_one == 3:
                chars[3] = chonk

    digits =[]
    for i in range(10):
        digits.append(chars[i])
    print(digits)

    value = []
    for ov in outputs[num]:
        value.append(str(digits.index(ov)))
    value = int(''.join(value))
    return value


    
    # for dig in outputs[num]:

#  _
# | |
#  -
# | |
#  -

sum = 0 
for i, reading in enumerate(readings):
    sum += analyze_line(i)

print ('sum ', sum)


