import numpy as np

def main():

	count = 0

	string = input("Please input a string: ")

	# for i in range(0, len(string)):
	# 	print(string[i])

	for i in range(0, len(string)-1):
		if string[i] >= 'A' and string[i] <= 'Z':
			if string[i-1] == ' ' or i == 0:
				print(string[i].upper(), end = '')
		elif (string[i] >= 'a' and string[i] <= 'z') and string[i-1] == ' ':
			print(string[i].upper(), end = '');

main()
print("")