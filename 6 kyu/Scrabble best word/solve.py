def get_best_word(points, words):
    index = 0
    max_score = 0
    length = 0

    for i, word in enumerate(words):
        score = sum(points[ord(c) - ord('A')] for c in word)

        if score > max_score or (score == max_score and len(word) < length):
            index = i
            max_score = score
            length = len(word)
    return index
