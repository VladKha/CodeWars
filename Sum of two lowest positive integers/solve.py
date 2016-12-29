def sum_two_smallest_numbers(numbers):
    min1, min2 = numbers[0:2]

    for i in range(2, len(numbers)):
        if numbers[i] < min2 and numbers[i] < min1:
            min1 = numbers[i]
        elif min1 < numbers[i] < min2:
            min2 = numbers[i]

    return min1 + min2
