import re


def solution(s, markers):
    if not markers:
        return s.strip()
    pattern = re.compile(
        ' *[{}].*\n'
            .format(''.join([m if m not in '-^' else '\\' + m for m in markers]))
    )
    return re.sub(pattern, '\n', s + '\n')[:-1]
