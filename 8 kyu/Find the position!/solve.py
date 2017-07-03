from string import ascii_lowercase as alphabet


def position(letter):
    return 'Position of alphabet: {}'.format(alphabet.index(letter.lower()) + 1)
