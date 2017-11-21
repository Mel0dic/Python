'''
Python program to encrypt given scentence with given key
'''

import sys

#Function to check if charachter is a lower case letter
def islower(char):
	#If the ascii number of the char is >= than the ascii number of lower case a and <= than the number of lower case z return true
	if (ord(char) >= ord('a')) and (ord(char) <= ord('z')):
		return True
	else:
		return False

#Function to check if charachter is a upper case letter
def isupper(char):
	#If the ascii number of the char is >= than the ascii number of capital A and <= than the number of capital Z return true
	if(ord(char) >= ord('A')) and (ord(char) <= ord('Z')):
		return True
	else:
		return False


def viginere(keyword):
	#Input the text to be encrypted by the keyword given
	ctext = input("Enter the cipher text: ")

	#Set counts to 0
	counts = 0
	#Set cline to the length of the keyword	
	cline = len(keyword)
	#Initialize ctexta array	
	ctexta = []
	#Initialize key array
	key = []

	#For letter in the ctext append the cipher text array with the letter 
	for i in range(0, len(ctext)):
		ctexta.append(ctext[i])

	#For i in range(0, length of keyword)
	for i in range(0, cline):
		#If keyword letter is a lower case letter
		if islower(keyword[i]):
			#Append the key with the letter offset
			#If letter was b - a so the key gets appended with 1	
			key.append(ord(keyword[i]) - ord('a'))
		#If letter is a uppercase letter
		elif isupper(keyword[i]):
			#Append the key with the letter offset
			#If letter was B - A so the key gets appended with 1
			key.append(ord(keyword[i]) - ord('A'))
		#If the letter not upper or lower case so not a letter
		else:
			#Append the key array with the asccii number for the char
			key.append(ord(keyword[i]))

	#For i in range(0, length of cypher text array(ctexta))
	for i in range(0, len(ctexta)):
		#If letter is lower case
		if islower(ctexta[i]):
			#print out the char version of the number worked out by...
			#getting the ascii number of letter - 97(the ascii of 'a') + the key number then % 26 to make sure we are still a letter between (0, 26) then add ascii num of 'a'
			print(chr((((ord(ctexta[i]) - 97)+key[counts])% 26)+97), end = '')
			#Add 1 to counts
			counts += 1
		#If letter is upper case
		elif isupper(ctexta[i]):
			#print out the char version of the number worked out by...
			#getting the ascii number of letter - 65(the ascii of 'A') + the key number then % 26 to make sure we are still a letter between (0, 26) then add ascii num of 'A'
			print(chr((((ord(ctexta[i]) - 65)+key[counts])% 26)+65), end = '')
			#Add 1 to counts
			counts += 1
		#If letter is not a letter
		else:
			#Print char with no endline
			print(ctexta[i], end = '')
		#If counts is == to keyword length	
		if counts == cline:
			#Set counts to 0	
			counts = 0
	#Print new line
	print('\n')

def main():
	#If there is no argument after program call eg python viginere.py (key word)
	if len(sys.argv) > 1:
		#Call function with argument
		viginere(sys.argv[1])
	else:
		print("Error: python3 viginere.py (key word)")


if __name__ == "__main__":
	main()