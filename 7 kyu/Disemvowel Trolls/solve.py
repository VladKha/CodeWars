def disemvowel(s):
    return ''.join(ch for ch in s if ch.lower() not in 'aeiou')
