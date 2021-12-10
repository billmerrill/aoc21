"""
): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
"""
openers = set(['(', '[', '{', '<'])
closers = set([')', ']', '}', '>'])
delims = [('(', ')'),
          ('[', ']'),
          ('{', '}'),
          ('<', '>')]


def score_line(line):
    stack = []
    for i in line.strip():
        if i in openers:
            stack.append(i)
        else:
            match i:
                case ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        print("illegal match", stack[-1], i)
                        return 3
                case ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        print("illegal match", stack[-1], i)
                        return 57 
                case '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        print("illegal match", stack[-1], i)
                        return 1197
                case '>':
                    if stack[-1] == '<':
                        stack.pop()
                    else:
                        print("illegal match", stack[-1], i)
                        return 25137

    return 0


# fh = open('ex.txt', 'r')
fh = open('input.txt', 'r')
scores = []
for line in fh.readlines():
    scores.append(score_line(line))

print(sum(scores))