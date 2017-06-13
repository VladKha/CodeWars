from string import ascii_lowercase as alphabet


def encode(s):
    def f(ch):
        if ch.lower() in alphabet:
            i = alphabet.index(ch.lower())
            return str(i % 2)
        return ch
    return ''.join(map(f, s))
