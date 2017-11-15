num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print(num1 + num2)
print(num1 * num2)
print(num1 ** num2)

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
# num4 = int(input("Enter number 4: "))

# print((num1 + num2 + num3 + num4) / 4)
numbers = []
for i in range(0, 4):
	numbers.append(int(input("Enter number {}: ".format(i))))

print((numbers[0] + numbers[1] + numbers[2] + numbers[3]) / 4)

numbers.sort()

print((numbers[2] + numbers[3])/2)