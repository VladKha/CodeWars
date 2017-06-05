import math


def solution(a):
    result = ''

    tmp = []
    for e in a:
        if not tmp or math.fabs(e - tmp[-1]) == 1:
            tmp.append(e)
        else:
            if len(tmp) >= 3:
                result += '{}-{},'.format(tmp[0], tmp[-1])
            else:
                for t in tmp:
                    result += '{},'.format(t)
            tmp = [e]
    if len(tmp) >= 3:
        result += '{}-{},'.format(tmp[0], tmp[-1])
    else:
        for t in tmp:
            result += '{},'.format(t)

    return result[:-1]
