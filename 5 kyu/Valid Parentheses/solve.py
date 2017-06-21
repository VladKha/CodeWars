def valid_parentheses(string):
    i = 0
    for c in string:
        if c == '(':
            i += 1
        if c == ')':
            i -= 1
        if i < 0:
            return False
    return i == 0
