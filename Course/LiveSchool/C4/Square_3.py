def getValue():
	try:
		Square = int(input("Enter a number: "))
	except ValueError:
		print("Please Enter A number")
		Square = getValue()
	return Square

while 1:
	print(getValue() ** 2)