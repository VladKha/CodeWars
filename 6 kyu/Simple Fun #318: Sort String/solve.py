def sort_string(s):
    letters = iter(sorted((c for c in s if c.isalpha()), key=str.lower))
    return ''.join(next(letters) if c.isalpha() else c for c in s)
