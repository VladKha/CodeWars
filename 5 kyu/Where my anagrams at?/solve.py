from collections import Counter


def anagrams(word, words):
    c = Counter(word)
    return [w for w in words if Counter(w) == c]
