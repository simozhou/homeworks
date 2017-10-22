from collections import OrderedDict
d,n = OrderedDict(), int(input())
for _ in range(n):
    word = input()
    if word in d.keys():
        d[word] += 1
    else:
        d[word] = 1

a, b = len(d), d.values()
print(a)
print(*b, sep=' ')