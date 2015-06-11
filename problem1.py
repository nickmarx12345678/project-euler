total = 0
common = set()
for i in range(0, 1000, 3):
    total += i
    if i % 5 == 0:
        common.add(i)

for i in range(0, 1000, 5):
    if not i in common:
        total += i

print total
