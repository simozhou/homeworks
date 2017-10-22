from collections import Counter
n = input()
tot_shoes = Counter(map(int, raw_input().split()))
c = input()
customers = [tuple(map(int,raw_input().split())) for _ in xrange(c)]

balance = 0

for size, price in customers:
    if size in tot_shoes.keys() and tot_shoes[size] != 0:
        balance += price
        tot_shoes[size] -= 1
print balance