#For loop ranging from 1 to 100
for i in range(1, 101):
	#Inistalize fizzBuzz as an empty string
	fizzBuzz = ""
	#If dividing i by 3 leaves no remainder add Fizz to string
	if i % 3 == 0:
		fizzBuzz += "Fizz"
	#If dividing i by 5 leaves no remainder add Buzz to string
	if i % 5 == 0:
		fizzBuzz += "Buzz"
	#If string is still empty add i to the string
	if fizzBuzz == "":
		fizzBuzz += str(i)
	#Print whatever is in the string	
	print(fizzBuzz)