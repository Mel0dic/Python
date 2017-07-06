import random

def main():
	name = input("What is your name? ")
	print("Well, " + name + ", I am thinking of a number between 1 and 20")

	secretNumber = random.randint(1, 20)

	for guesses in range(0, 7):
		guess = int(input("Try guess the number I am thinking: "))

		if guess < secretNumber:
			print("Too low")
		elif guess > secretNumber:
			print("Too high")
		else:
			break
	if guess == secretNumber:
		print("Congratz")
	else:
		print("Out of guesses")

if __name__ == "__main__":
	main()