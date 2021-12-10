"""
): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
"""
import statistics

openers = set(['(', '[', '{', '<'])
closers = set([')', ']', '}', '>'])
delims = [('(', ')'),
          ('[', ']'),
          ('{', '}'),
          ('<', '>')]
pairs = {}

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
incomplete_lines = []
for line in fh.readlines():
    score = score_line(line)
    scores.append(score)
    if score == 0:
        incomplete_lines.append(line)
print('invalid score')
print(sum(scores))
print('\n')


marks = {'{':'}', '(':')', '[':']', '<':'>'}
rmarks = {'}':'{', ')':'(', ']':'[', '>':'<'}

def build_needs(line):
    stack = []
    for i in line.strip():
        if i in openers:
            stack.append(i)
        else:
            if stack[-1] == rmarks[i]:
                stack.pop()
    return stack

mark_score = {'{':3, '(':1, '[':2, '<':4}
incom_scores = []
for line in incomplete_lines:
    needs = build_needs(line)
    score = 0
    for i in reversed(needs):
        score *= 5
        score += mark_score[i]
    incom_scores.append(score)

print('mid score')
print(statistics.median(sorted(incom_scores)))
