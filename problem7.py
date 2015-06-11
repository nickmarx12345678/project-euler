#3 seconds?
import math

def nth_prime(n):
    primes = [2]
    potential_prime = 3
    while len(primes) < n:
        if is_prime(potential_prime, primes):
            primes.append(potential_prime)
        potential_prime += 2
    return primes[-1]


def is_prime(n, options):
    for option in options:
        if n % option == 0:
            return False
    return True

print nth_prime(10001)
