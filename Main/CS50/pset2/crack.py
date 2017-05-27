import sys, crypt

def plusplus(cstring, some):
	if cstring[some] is '':
		cstring[some] = 'a'
	elif cstring[some] == 'z':
		cstring[some] = 'A'
	elif cstring[some] == 'Z':
		cstring[some] = 'a'
		plusplus(cstring, (some+1))
	else:
		cstring[some] = chr(ord(cstring[some]) + 1)

def decrypt(key, salt):
	passs = ['', '', '', '', '']

	print(passs)
	print(key)

	while passs[4] is '':
		print("%s and %s which == %s" %(key, crypt.crypt(''.join(passs), salt), ''.join(passs)))
		if key == crypt.crypt(''.join(passs), salt):
			print("The Password Is: %s" %(''.join(passs)))
			return 1
		plusplus(passs,0)

	return 0


def main():
	salt = "00"
	if len(sys.argv) == 2:
		salt = sys.argv[1][:2] + salt[2:]
		decrypt(sys.argv[1], salt)
	else:
		print("Error: python3 crack.py (key)")
main()