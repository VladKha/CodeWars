def alphabet_position(text):
    return ' '.join(str(ord(c)-ord('a')+1) for c in text.lower() if c.isalpha())

