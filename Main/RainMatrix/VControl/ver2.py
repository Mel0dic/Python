import sys, time, random, os
from reprint import output

os.system('cls')

row, column = os.get_terminal_size()

refresh = 20

letters = ["0", "1", " "]

arrs = [[" "] * row] * column

STRINGER = ""

with output(output_type = "list", initial_len = 3, interval = 0) as outputLines:
	for i in range(refresh):
		for x in range(column):
			for z in range(row):
				arrs[x][0] = letters[random.randint(0, 2)]
			STRINGER += "".join(arrs[x])
		outputLines[False] = STRINGER
		STRINGER = ""
		time.sleep(0.1)

os.system('cls')