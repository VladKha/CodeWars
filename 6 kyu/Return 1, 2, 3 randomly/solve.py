import random


def one_two():
    return random.randint(1, 2)


def one_two_three():
    a, b = one_two(), one_two()
    return {(1, 1): 1, (1, 2): 2, (2, 1): 3, (2, 2): 0}[(a, b)] or one_two_three()
