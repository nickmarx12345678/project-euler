
num = 2**1000

total = 0
while num > 10:
	rem = num % 10
	num = num/10
	total += rem
#add final remainder, probably a cleaner way to do this
print total+num
