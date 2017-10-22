from itertools import combinations
N, L, K = input(), raw_input().split(), input()
combos = list(combinations(L, K))
print len(filter(lambda x: 'a' in x, combos))/float(len(combos))