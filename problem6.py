
sumsquares = 0
for i in range(1, 101):
    print i
    sumsquares += i**2

squaresum = sum(range(1, 101))**2

print sumsquares - squaresum
