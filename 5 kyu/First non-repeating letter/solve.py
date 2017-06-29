from collections import Counter


def first_non_repeating_letter(s):
    counts = Counter(s.lower())
    for ch in s:
        if counts[ch.lower()] == 1:
            return ch
    return ''
