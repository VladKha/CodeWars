def remove(text, what):
    for c, n in what.items():
        text = text.replace(c, '', n)
    return text
