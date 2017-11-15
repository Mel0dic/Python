def factorial(factor):
	if factor == 0:
		return 1
	return factor * factorial(factor-1)

print(factorial(int(input("Enter your number to factor? "))))
