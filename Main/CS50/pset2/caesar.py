import sys

def islower(char):
	if (ord(char) >= ord('a')) and (ord(char) <= ord('z')):
		return True
	else:
		return False

def isupper(char):
	if(ord(char) >= ord('A')) and (ord(char) <= ord('Z')):
		return True
	else:
		return False

def caesar(word, num):
	for i in word:
		if islower(i):
			number = ord(i)
			numb = (((number - 97)+int(num))% 26)+97
			i = chr(numb)
		elif isupper(i):
			number = ord(i)
			numb = (((number - 65)+int(num))% 26)+65;
			i = chr(numb)
	print(word)
	return word

def main(num):
	sipher = input("Please enter a word or sentence: ")
	caesar(sipher, num)


if len(sys.argv) > 1:
	main(sys.argv[1])
else:
	print("Error: python3 caesar.py (sipher)")