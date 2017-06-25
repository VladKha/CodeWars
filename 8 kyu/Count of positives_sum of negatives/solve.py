def count_positives_sum_negatives(a):
    if not a:
        return []
    counter, neg_sum = 0, 0
    for x in a:
        if x > 0:
            counter += 1
        else:
            neg_sum += x
    return [counter, neg_sum]
