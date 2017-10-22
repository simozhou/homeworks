def count_substring(string, sub_string):
    counter = 0
    l = len(sub_string)
    l_s = len(string)-len(sub_string)
    for i in xrange(l_s+1):
        j = i + l
        if string[i:j] == sub_string:
            counter += 1
    return counter