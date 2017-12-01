from collections import Counter


def palindrome_rearranging(s):
    c = Counter(s)
    odd = 0
    possible = True
    for v in c.values():
        if v % 2 != 0:
            odd += 1
        if odd > 1:
            possible = False
            break
    return possible
