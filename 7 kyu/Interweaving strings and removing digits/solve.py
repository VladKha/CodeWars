def interweave(s1, s2):
    result = ''
    i = 0
    while i < len(s1) or i < len(s2):
        if i < len(s1) and not s1[i].isdigit():
            result += s1[i]
        if i < len(s2) and not s2[i].isdigit():
            result += s2[i]
        i += 1
    return result
