import re


def reverse_words(s):
    return re.sub(r'\S+', lambda w: w.group(0)[::-1], s)
