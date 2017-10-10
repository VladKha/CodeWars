def move_vowels(s):
    result = ''
    vowels = ''
    for c in s:
        if c in 'aeiou':
            vowels += c
        else:
            result += c
    return result + vowels
