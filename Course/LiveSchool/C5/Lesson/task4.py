import random

numbers = []

while 1:
	numbers.append(int(input("Enter a number or -1 to stop: ")))
	if numbers[len(numbers)-1] == -1:
		numbers.pop(len(numbers)-1)
		break

total = 0
for i in numbers:
	total = total + i

print(total)
print(total/len(numbers))
print(max(numbers) - min(numbers))
