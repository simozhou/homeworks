VOW = 'AEIOU'

def minion_game(string):
    kevin, stuart = 0, 0 #vowels, consonants
    for k,v in enumerate(s):
        if v in VOW:
            kevin += len(s)-k
        else:
            stuart += len(s)-k
         
    if kevin > stuart:
        print 'Kevin %d' % kevin
    elif kevin < stuart:
        print 'Stuart %d' % stuart
    else:
        print 'Draw'
    