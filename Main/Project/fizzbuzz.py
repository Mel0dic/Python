def main():
	output = ""
	for i in range(0, 101):
		if i % 3 == 0:
			output += "Fizz"
		if i % 5 == 0:
			output += "Buzz"
		if output == "":
			print(i)
		else:
			print(output)
			output = ""

if __name__ == "__main__":
	main()