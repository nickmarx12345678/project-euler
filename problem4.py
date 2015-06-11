def is_pallindrome(num):
    strnum = str(num)
    return strnum == strnum[::-1]

best = 1
for i in range(999):
    for j in range(999):
        num = i*j
        if num > best and is_pallindrome(num):
            best = num

print best
