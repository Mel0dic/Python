'''

Modularity (OOP) - Object oriented programming. Using objects
Modularity (Procedural)
Argument - An argument something that you pass in a function so that you can use that data point in the function.
Function - Something callable to execute a set of instructions.
Subroutine
Variable - Something that holdnds a piece of data and that you can hold.
Data type - Something that is held in a variable
Constant
Local Variable - A variable accessable in only the function it is declared
Parameter
Procedure
Scope
Global Variable - A variable accessable throughout the program in all functions.

Blocks of Code
	-
	-
Passing Data
	-
	-
Who can see what
	-
	-
What am I?
	-
	-

'''

def main():
	#for i in range(1, 11):
	# 	print(i ** 2)
	for i in range(2, 101):
		if isPrime(i):
			print(i)

def isPrime(query):
	for i in range(2, query):
		if query % i == 0:
			return False
	return True

if __name__ == "__main__":
	main()