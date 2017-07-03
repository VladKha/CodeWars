def replace_exclamation(s):
    vowels = 'aeiouAEIOU'
    return ''.join('!' if c in vowels else c for c in s)
