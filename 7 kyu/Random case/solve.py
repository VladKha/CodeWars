import random


def random_case(s):
    return ''.join(random.choice([x.lower(), x.upper()]) for x in s)
