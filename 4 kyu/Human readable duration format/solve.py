def format_duration(s):
    if s == 0:
        return 'now'

    result_list = []
    rest = s
    for divisor, name in zip([60, 60, 24, 365, float('inf')], ['second', 'minute', 'hour', 'day', 'year']):
        value = int(rest % divisor)
        rest = (rest - value) // divisor
        if value:
            s = '{} {}'.format(value, name)
            if value > 1:
                 s += 's'
            result_list.append(s)

    result_list.reverse()

    if len(result_list) > 1:
        return ', '.join(result_list[:-1]) + ' and ' + result_list[-1]

    return result_list[-1]
