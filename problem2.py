
def is_even(num):
    return num % 2 == 0


prevprev = 1
prev = 2
current = 3
total = 2

while current < 4000000:
    prevprev = prev
    prev = current
    current = prevprev + prev

    if is_even(current):
        total += current
print total
