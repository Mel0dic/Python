"""
MY AWNSER
"""

files = open("myLetters.txt", "w")

for i in range(0, 26):
	files.write(chr(i + 97) + "\n")

"""
THE AWNSER
"""

import string
 
with open("letters.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")