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

def viginere(keyword):
	ctext = input("Enter the cipher text: ")


	counts = count = 0
	cline = len(keyword)
	ctexta = []
	key = []

	for i in range(0, len(ctext)):
		ctexta.append(ctext[i])

	for i in range(0, cline):
		if islower(keyword[i]):
			key.append(ord(keyword[i]) - ord('a'))
		elif isupper(keyword[i]):
			key.append(ord(keyword[i]) - ord('A'))
		else:
			key.append(ord(keyword[i]))

	for i in range(0, len(ctexta)):
		if islower(ctexta[i]):
			print(chr((((ord(ctexta[i]) - 97)+key[counts])% 26)+97), end = '')
			counts += 1
		elif isupper(ctexta[i]):
			print(chr((((ord(ctexta[i]) - 65)+key[counts])% 26)+65), end = '')
			counts += 1
		else:
			print(ctexta[i], end = '')
		if counts == cline:
			counts = 0
	print('\n')

def main():
	if len(sys.argv) > 1:
		viginere(sys.argv[1])
	else:
		print("Error: python3 viginere.py (key word)")

main()