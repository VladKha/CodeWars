from collections import Counter


def mix(s1, s2):
    count1 = Counter(filter(str.islower, s1))
    count2 = Counter(filter(str.islower, s2))

    parts = []
    for c in set(count1.keys() | count2.keys()):
        n1, n2 = count1.get(c, 0), count2.get(c, 0)
        if n1 > 1 or n2 > 1:
            if n1 > n2:
                parts.append('1:' + c * n1)
            elif n1 < n2:
                parts.append('2:' + c * n2)
            else:
                parts.append('=:' + c * n1)

    return '/'.join(sorted(parts, key=lambda s: (-len(s), s)))
