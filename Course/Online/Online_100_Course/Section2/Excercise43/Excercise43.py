import string

sideA = string.ascii_lowercase[0::2]
sideB = string.ascii_lowercase[1::2]

with open("alpha.txt", "w") as file:
	for i, j in zip(sideA, sideB):
		file.write(i + j + "\n")