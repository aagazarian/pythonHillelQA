import math


def square(a):
    p = 4 * a
    s = a * a
    k = math.sqrt(2)
    l = a * k
    result = [p, s, l]
    return tuple(result)


print(square(2))


