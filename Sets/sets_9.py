n = input()
eng = set(map(int, raw_input().split()))
m = input()
fra = set(map(int, raw_input().split()))

print len(eng.union(fra)-eng.intersection(fra))