def filter_long_words(sentence, n):
    return [w for w in sentence.split() if len(w) > n]
