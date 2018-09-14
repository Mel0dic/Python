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
	arr = []
	for i in range(0, len(word)):
		arr.append(word[i])
	for i in range(0, len(arr)):
		if islower(arr[i]):
			number = ord(word[i])
			numb = (((number - 97)+int(num))% 26)+97
			arr[i] = chr(numb)
		elif isupper(arr[i]):
			number = ord(word[i])
			numb = (((number - 65)+int(num))% 26)+65;
			arr[i] = chr(numb)
	print(arr)
	return word

def main(num):
	sipher = input("Please enter a word or sentence: ")
	caesar(sipher, num)

if len(sys.argv) > 1:
	main(sys.argv[1])
else:
	print("Error: python3 caesar.py (sipher)")