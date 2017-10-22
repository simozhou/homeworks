from collections import OrderedDict
items = OrderedDict()
n = input()
for _ in xrange(n):
    item_string = raw_input().split()
    net_price = int(item_string.pop(-1))
    item_name = ' '.join(item_string)
    if item_name in items.keys():
        items[item_name] += net_price
    else:
        items[item_name] = net_price
    
for i in items.items():
    print '%s %d' % i