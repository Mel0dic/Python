import sys, time, random, os
from reprint import output
from time import time

os.system('cls')
row, column = os.get_terminal_size()
arrs = [[" "] * row for i in range(column)]
STRINGER = ""
Numbs = ["0", "1"]

class Symbol(self, x, y):
	def __init__(self);
		self.x = x
		self.y = y

	def setRandomSymbol(self):
		self.value = chr(0x30A0 + random.randint(0, 96))
		args[self.x, self.y] = self.value

class Stream(self, x, y, maxY, fallTime):
	def __init__(self):
		currentX = x
		currentY = y
		maxY = maxY #The smallest the y value can get before being cut off
		fallTime = fallTime #The point at which the line will start to fall
		birth = time()

	def getX(self):
		return self.currentX

	def update(self):
		flytime = time - self.birth



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



	for i in range(column):
		if arrs[0][i] in Numbs:
			arrs[0][i] == Numbs[random.randint(0, 1)]
		STRINGER += "".join(arrs[x])
	outputLines[0] = STRINGER
	STRINGER = ""
	time.sleep(0.1)

os.system('cls')