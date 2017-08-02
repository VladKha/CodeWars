def find_missing(sequence):
    step = (sequence[-1] - sequence[0]) / len(sequence)
    next_number = sequence[0]
    for i in range(len(sequence)-1):
        if next_number != sequence[i]:
            return next_number
        next_number += step
