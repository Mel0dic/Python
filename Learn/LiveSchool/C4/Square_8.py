def getValue():
	try:
		Square = int(input("Enter a number or enter -1 to quit: "))
	except ValueError:
		print("Please Enter A number")
		Square = getValue()
	return Square

while 1:
	enteredValue = getValue()
	if enteredValue == -1:
		break
	else:
		print(enteredValue ** 2)