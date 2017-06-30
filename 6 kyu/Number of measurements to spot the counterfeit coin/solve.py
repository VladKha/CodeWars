import math


def how_many_measurements(n):
    return math.ceil(math.log(n, 3))

# Another solution
# import math
# from functools import lru_cache
#
#
# @lru_cache(None)
# def how_many_measurements(n):
#     if n == 1:
#         return 0
#     elif 2 <= n <= 3:
#         return 1
#     return 1 + how_many_measurements(math.ceil(n/3))
