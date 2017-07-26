import math

def liqVol(h, radius = 10):
	pA = ((4 * math.pi * radius**3) / 3)
	pB = (math.pi * h**2 * (3 * radius - h) / 3)
	return pA - pB

print(liqVol(2))