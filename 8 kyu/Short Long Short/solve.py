def solution(a, b):
    return '{0}{1}{0}'.format(*sorted((a, b), key=len))
