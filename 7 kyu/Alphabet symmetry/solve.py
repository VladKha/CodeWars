from string import ascii_lowercase as alphabet


def solve(arr):
    return [sum(c == alphabet[i] for i,c in enumerate(word[:26].lower())) for word in arr]
