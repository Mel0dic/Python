import random

numbers = []

for i in range(0, random.randrange(1, 5)):
	numbers.append(int(input("Enter a number: ")))

numbers.sort()