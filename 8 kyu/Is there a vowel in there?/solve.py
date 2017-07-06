def is_vow(s):
    vowels = {ord(c): c for c in 'aouei'}
    return [vowels.get(a, a) for a in s]
