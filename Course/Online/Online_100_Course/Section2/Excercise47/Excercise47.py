"""
for file in "./letters":
	read file
	array.append file contents
"""

import glob

read = []
word = "python"

for i in glob.glob("letters/*.txt"):
	with open(i, "r") as file:
		if file.read() in word:
			print(file.read())
			read.append(file.read())

read.sort()
print(read)