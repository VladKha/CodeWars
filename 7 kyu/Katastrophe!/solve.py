import math
from functools import reduce


def strong_enough(earthquake, age):
    strength = 1000 * math.e ** (-0.01*age)
    magnitude = reduce(lambda x,y: x*y, [sum(shockwave) for shockwave in earthquake])
    return 'Safe!' if strength - magnitude > 0 else 'Needs Reinforcement!'
