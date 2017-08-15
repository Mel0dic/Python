import string

sideA = string.ascii_lowercase[0::3]
sideB = string.ascii_lowercase[1::3]
sideC = string.ascii_lowercase[2::3]

with open("alpha.txt", "w") as file:
	for i, j, y in zip(sideA, sideB, sideC):
		file.write(i + j + y + "\n")