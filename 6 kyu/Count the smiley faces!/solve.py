import re

SMILE = r'[:;][-~]?[\)D]'


def count_smileys(arr):
    return sum(bool(re.match(SMILE, x)) for x in arr)
