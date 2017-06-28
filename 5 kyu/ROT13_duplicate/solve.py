import codecs


def rot13(message):
    return codecs.encode(message, 'rot_13')
