import re


def sum_of_integers_in_string(s):
    return sum(map(int, re.findall(r'\d+', s)))
