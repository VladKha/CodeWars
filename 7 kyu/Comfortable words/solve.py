def comfortable_word(word):
    left = 'qwertasdfgzxcvb'
    right = 'yuiophjklnm'
    n = len(word)

    start_left = word[0] in left
    if start_left:
        return all(word[i] in left for i in range(0, n, 2)) and all(word[i] in right for i in range(1, n, 2))
    else:
        return all(word[i] in right for i in range(0, n, 2)) and all(word[i] in left for i in range(1, n, 2))
