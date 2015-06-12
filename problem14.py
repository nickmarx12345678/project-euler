

def collatz_rec(n, memo):
    if n in memo:
        return memo[n]

    if is_even(n):
        memo[n] = 1 + collatz_rec(n/2, memo)
    else:
        memo[n] = 1 + collatz_rec(3*n + 1, memo)
    return memo[n]


def is_even(n):
    return n % 2 == 0

memo = {1:1}

for i in range(1, 1000000):
    collatz_rec(i, memo)


best_val = 0
best_start = None
for key in memo:
    if memo[key] > best_val:
        best_val = memo[key]
        best_start = key
        print "new best ",best_start, best_val
