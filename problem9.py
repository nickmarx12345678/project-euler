import math

for a in range(0,250):
	for b in range(a,500):
		c = 1000 - (b+a)
		if a**2 + b**2 == c**2:
			print a,b,c
			print a*b*c