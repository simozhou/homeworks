if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    print [ [ i, j, z] for i in xrange( x + 1) for j in xrange( y + 1) for z in xrange( z + 1) if ( ( i + j + z) != n )]