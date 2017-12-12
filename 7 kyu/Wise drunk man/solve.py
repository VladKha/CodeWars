def wdm(talk):
    return ' '.join(word for word in talk.split() if word.lower() not in ['puke', 'hiccup'])
