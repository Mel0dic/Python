import sys, time, random, os
from reprint import output

os.system('cls' if os.name == 'nt' else 'clear')

column, row = os.get_terminal_size()
row -= 1

arrs = [[" "] * column for i in range(row)]

STRINGER = ""
Numbs = ["0", "1"]

class Symbol:
	def __init__(self, x, y, speed):
		self.row = int(x)
		self.column= int(y)
		self.speed = speed

	def setRandomSymbol(self):
		self.value = chr(0x30A0 + random.randint(0, 96))
		arrs[self.row][self.column]= self.value

	def rain(self):
		self.column += self.speed

symb = Symbol(0, column/2, 1)
symb.setRandomSymbol()

with output(output_type = "list", initial_len = 3, interval = 0) as outputLines:
	while 1:
		for i in range(row):
			STRINGER += "".join(arrs[i])
		symb.rain()
		outputLines[0] = STRINGER
		STRINGER = ""
		time.sleep(1)	

#print(STRINGER)
#print(arrs[int(column/2)][int(row/2)])