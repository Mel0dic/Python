import sys, time, random, os
from reprint import output

os.system('cls')
row, column = os.get_terminal_size()
arrs = [[" "] * row for i in range(column)]
STRINGER = ""

with output(output_type = "list", initial_len = 3, interval = 0) as outputLines:

	for x in range(column):
		for z in range(row):
			if x == 0:
				chance = random.randint(0, 100)
				if chance < 5 and arrs[0][z-1] == " ":
					arrs[0][z] = "0"
				elif chance < 10 and arrs[0][z-1] == " ":
					arrs[0][z] = "1"
				else:
					arrs[0][z] = " "
		STRINGER += "".join(arrs[x])
	outputLines[0] = STRINGER
	STRINGER = ""
	time.sleep(0.1)

#os.system('cls')