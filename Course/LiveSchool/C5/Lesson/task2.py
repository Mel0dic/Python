num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 != num2:
	largest, smallest = (num1, num2) if num1 > num2 else (num2, num1)
	print(largest)
	print(largest - smallest)
else:
	print("The numbers are equal")

numbers = []
numbers.append(int(input("Enter number 1: ")))
numbers.append(int(input("Enter number 2: ")))
numbers.append(int(input("Enter number 3: ")))
numbers.append(int(input("Enter number 4: ")))

numbers.sort()
print(numbers[3] - numbers[1])