def average_string(s):
    if not s:
        return 'n/a'

    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    total = 0
    counter = 0
    for n in s.split():
        try:
            value = numbers.index(n)
            total += value
            counter += 1
        except:
            return 'n/a'
    return numbers[total // counter]
