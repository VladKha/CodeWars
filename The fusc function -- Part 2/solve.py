from test import test


''' First 'cheatty' solution '''
import sys
sys.setrecursionlimit(5000)

cache = {
    0: 0,
    1: 1
}


def fusc_(n):
    print(n)
    if n in cache:
        return cache[n]
    elif n % 2 == 0:
        result = fusc_(n // 2)
    else:
        result = fusc_(n // 2) + fusc_(n // 2 + 1)

    cache[n] = result
    return result


''' Second best solution '''
def fusc(n):
    a, b = 0, 1
    while n >= 1:
        if n % 2 == 0:
            b += a
        else:
            a += b
        n //= 2
    return a


''' TESTS '''
test.describe("The fusc function -- Part 2")
test.assert_equals(fusc(0), 0)
test.assert_equals(fusc(1), 1)
test.assert_equals(fusc((1<<1000) + 1), 1001)
test.assert_equals(fusc((1<<1000) - 1), 1000)
test.assert_equals(fusc((1<<1000) + 5), 2996)
test.assert_equals(fusc((1<<1000) + 21), 7973)