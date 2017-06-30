def merge(a, left_index, mid, right_index, aux):
    i, j = left_index, mid + 1
    inversions = 0

    for k in range(left_index, right_index + 1):
        aux[k] = a[k]

    for k in range(left_index, right_index + 1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > right_index:
            a[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            a[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1

            inversions += mid - i + 1
    return inversions


def count(a, left_index, right_index, aux):
    if right_index <= left_index:
        return 0
    mid = left_index + (right_index - left_index) // 2
    left_inversions = count(a, left_index, mid, aux)
    right_inversions = count(a, mid + 1, right_index, aux)
    return left_inversions + right_inversions + merge(a, left_index, mid, right_index, aux)


def count_inversion(sequence):
    if len(sequence) < 2:
        return 0
    aux = [None for _ in range(len(sequence))]
    sequence_list = list(sequence)
    return count(sequence_list, 0, len(sequence) - 1, aux)
