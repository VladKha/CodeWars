import re

def isDigit(s):
    return re.fullmatch(r'^\s*[+-]?[0-9]+(\.[0-9]+)?\s*$', s) is not None
