
def is_even(num):
    return num % 2 == 0

prev = 1
current = 2
total = 2

while current < 4000000:
    prevprev = prev
    prev = current
    current = prevprev + prev

    if is_even(current):
        total += current
print total
