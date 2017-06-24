def solution(digits):
    return max((int(digits[i:i+5]) for i in range(len(digits))))
