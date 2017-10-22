def print_formatted(number):
    hold = list()
    for i in xrange(1, number+1):
        deci, octa, hexa, bina = str(i), oct(i)[1:], hex(i)[2:].upper(), bin(i)[2:]
        hold.append([deci, octa, hexa, bina])
    max_width = len(hold[-1][-1]) #max binary length
    for i in xrange(len(hold)):
        deci = hold[i][0].rjust(max_width, ' ')
        octa = hold[i][1].rjust(max_width, ' ')
        hexa = hold[i][2].rjust(max_width, ' ')
        bina = hold[i][3].rjust(max_width, ' ')
        print deci, octa, hexa, bina