import string
from string import ascii_lowercase as alphabet


def rot13(message):
    result = ''
    for c in message:
        if c.isalpha():
            i = (alphabet.index(c.lower()) + 13) % len(alphabet)
            if c.islower():
                result += alphabet[i].lower()
            else:
                result += alphabet[i].upper()
        else:
            result += c
    return result
