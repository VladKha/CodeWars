from string import ascii_lowercase as alphabet


def decode(message):
    dictionary = str.maketrans(alphabet, alphabet[::-1])
    return message.translate(dictionary)
