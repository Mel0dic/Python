import numpy as np

def main():
	something = input("Please Input Your Card: ")
	something = cnum = int(something)
	count = 0

	while something > 0.99:
		something /= 10
		count += 1
	numb = np.zeros(count)

	for i in range((count-1), -1, -1):
		numb[i] = int(cnum % 10);
		cnum /= 10

	twos = count - 2
	trouble = test = 0

	while twos >= 0:
		if numb[twos] * 2 > 9:
			test += (numb[twos] * 2) % 10
			test += ((numb[twos] * 2) - ((numb[twos] * 2) % 10)) / 10
		else:
			test += numb[twos] * 2
		twos -= 2

	twos = count - 1

	while twos >= 0:
		trouble += numb[twos]
		twos -= 2

	if (test + trouble) % 10 == 0:
		if count == 15 and (numb[0] == 3 and (numb[1] == 7 or numb[1] == 4)):
			print("Amex")
		elif count == 16 and (numb[0] == 5 and (numb[1] == 1 or numb[1] == 2 or numb[1] == 3 or numb[1] == 4 or numb[1] == 5)):
			print("MasterCard")
		elif (count == 13 or count == 16) and (numb[0] == 4):
			print("Visa")
		else:
			print("\nInvalid Number\n")
	else:
		print("\nInvalid Number\n")
		
main()