marks = []
for _ in range(int(raw_input())):
    name = raw_input()
    mark = float(raw_input())
    marks.append([name, mark])

second = sorted(list(set([mark for name, mark in marks])))[1]
output = sorted([name for name, mark in marks if mark == second])
print '\n'.join(output)