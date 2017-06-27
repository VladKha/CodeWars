def solution(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]
