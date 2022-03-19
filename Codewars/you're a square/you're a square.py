from math import isqrt

is_square = lambda n: isqrt(n) ** 2 == n if n >= 0 else False

def is_square_soln(n):
    pass


print(is_square(-1))