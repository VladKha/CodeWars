import re


def replace_dots(s):
    return re.sub(r'\.', '-', s)
