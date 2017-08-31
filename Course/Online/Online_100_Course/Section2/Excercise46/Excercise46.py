"""
for file in "./letters":
	read file
	array.append file contents
"""

import glob

read = []

for i in glob.glob("letters/*.txt"):
	with open(i, "r") as file:
		read.append(file.read())

read.sort()
print(read)