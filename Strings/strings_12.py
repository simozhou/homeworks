def capitalize(string):
    string = list(string)
    if string[0].isalpha():
        string = [string[0].upper()] + string[1:]
    for i in xrange(1,len(string)):
        if string[i].isalpha() and string[i-1] == ' ':
            string[i] = string[i].upper()
    return ''.join(string)