def Square(Number):
		return Number ** 2

def getNumber():
	try:
		SquareNumber = int(input("Enter a number or enter -1 to quit: "))
		if SquareNumber != -1:
			print(Square(SquareNumber))
			getNumber()
	except ValueError:
		print("Please Enter A number")
		getNumber()

getNumber()