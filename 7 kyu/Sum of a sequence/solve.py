def sequence_sum(begin_number, end_number, step):
    if end_number < begin_number:
        return 0
    n = (end_number - begin_number) // step
    end_number = begin_number + n * step
    return (begin_number + end_number) * (n + 1) / 2
