
def gcp(n):
    i = 2
    while i*i < n:
        while n % i == 0: #while num divisible by factor
            n = n / i
        i+=1
    return n

print gcp(600851475143)
