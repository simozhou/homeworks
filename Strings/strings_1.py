def is_alpha(m):
    if m in 'abcdefghijklmnopqrstuvwyxz':
        return True
    else:
        return False

def swap_case(s):
    holder = list()
    for i in s:
        if i.isupper():
            i = i.lower()
        elif not is_alpha(i):
            holder.append(i)
            continue
        else:
            i= i.upper()
        holder.append(i)
    return ''.join(holder)