if __name__ == '__main__':
    N = int(raw_input())
    L = list()
    for i in xrange(N):
        inp = raw_input().split()
        func = inp.pop(0)
        if func == 'print':
            print L
        else:
            cmd = 'L.'+func+'('+','.join(inp)+')'
            eval(cmd)