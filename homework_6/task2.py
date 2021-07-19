import math
from typing import Union


def square(a):
    p = 4 * a
    s = a * a
    k = math.sqrt(2)
    l = a * k
    result = [p, s, l]
    return tuple(result)


print(square(2))

# Good. But names of variables does not highlight purpose of objects.
# Not clear what is p, s, k, l.
# there are not sense aggregate variables into the list and convert it into the
# tuple. Take a look how will be cleaner and better even without annotations^
# def square(side):
#     perimeter, area, diagonal = 4 * side, side * side, side * math.sqrt(2)
#     return perimeter, area, diagonal
# or
# def square(side):
#     """
#         Calculates perimeter, area and diagonal of square and return in tuple
#     """
#
#     return 4 * side, side * side, side * math.sqrt(2)
