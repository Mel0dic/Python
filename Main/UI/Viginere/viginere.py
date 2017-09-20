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

def viginere(keyword, ctext):


	counts = count = 0
	cline = len(keyword)
	ctexta = []
	key = []
	word = []

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
			word.append(chr((((ord(ctexta[i]) - 97)+key[counts])% 26)+97))
			counts += 1
		elif isupper(ctexta[i]):
			word.append(chr((((ord(ctexta[i]) - 65)+key[counts])% 26)+65))
			counts += 1
		else:
			word.append(ctexta[i])
		if counts == cline:
			counts = 0
	return ''.join(word)

def main():
	if len(sys.argv) > 1:
		ctext = input("Enter what you want to be encoded: ")
		viginere(sys.argv[1], ctext)
	else:
		print("Error: python3 viginere.py (key word)")


if __name__ == "__main__":
	main()