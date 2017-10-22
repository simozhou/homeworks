n, set1, n, set2 = input(), set(map(int,raw_input().split())), input(), set(map(int,raw_input().split()))
for i in sorted(set1.union(set2) - set1.intersection(set2)):
    print i

