
def primes_under_n(n):
    primes = [True] * n
    primes[0] = primes[1] = False

    for (i, is_prime) in enumerate(primes):
        if is_prime:
            yield i
            for j in xrange(i*i, n, i):
                primes[j] = False

total = 0
for prime in primes_under_n(2000000):
    total += prime

print total
