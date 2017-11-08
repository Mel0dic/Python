def getValue():
	try:
		Square = int(input("Enter a number: "))
	except ValueError:
		print("Please Enter A number")
		Square = getValue()
	return Square

print(getValue() ** 2)