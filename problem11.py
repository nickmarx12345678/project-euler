import math


def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

i = 7
triangle = 28
while True:
    if len(factors(triangle)) > 500:
        print triangle
        break
    i += 1
    triangle += i
