alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def print_rangoli(size):
    hold = []
    for i in range(size):
        s = "-".join(alph[i:size])
        hold.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(hold[:0:-1]+hold))