current = 20
divisors = [11,12,13,14,15,16,17,18,19] #implicitly remove subfactors
divisors.reverse()
while True:
    found = True
    for i in divisors:
        if not current % i == 0:
            found = False
            break
    if found:
        print current
        break
    else:
        current += 20
