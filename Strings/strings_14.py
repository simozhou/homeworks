from collections import OrderedDict
def merge_the_tools(string, k):
    hold=[]
    for i in range(0, len(string), k):
        hap = OrderedDict()
        for j in string[i:i+k]:
            hap[j] = None
        hold.append(''.join(hap.keys()))
            
    for i in hold:
        print(i)