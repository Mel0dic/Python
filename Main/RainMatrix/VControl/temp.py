import sys, time, random, os
from reprint import output





os.system('cls' if os.name == 'nt' else 'clear')

column, row = os.get_terminal_size()

symbolSize = 1

arrs = [[" "] * column for i in range(row)]





def main():
	global arrs, column, row

	STRINGER = ""
	Numbs = ["0", "1"]
	stream = Stream()
	stream.generateSymbols()

	with output(output_type = "list", initial_len = 3, interval = 0) as outputLines:
		while 1:
			for i in range(row):
				STRINGER += "".join(arrs[i])
			stream.render()
			outputLines[0] = STRINGER
			STRINGER = ""
			time.sleep(0.1)	




class Symbol:
	def __init__(self, x, y, speed):
		self.row = int(x)
		self.column= int(y)
		self.speed = speed
		self.switchInterval = 0
		self.value = None

	def setRandomSymbol(self):
		if self.switchInterval <= 25:
			#self.value = chr(0x30A0 + random.randint(0, 96)) ##### Problem with char size pushing lines breaks shit fuck that
			self.value = str(random.randint(1, 0))
			arrs[self.row][self.column] = self.value
		self.symbolSwitch()

	def rain(self):
		self.row = 0 if self.row + self.speed >= row else self.row + self.speed

	def symbolSwitch(self):
		self.switchInterval = random.randint(1, 100)





class Stream:
	def __init__(self):
		self.symbols = []
		self.totalSymbols = random.randint(3, 10)
		#self.speed = random.randint(1,3)
		self.speed = 1

	def generateSymbols(self):
		y = column/2
		x = 0

		for i in range(0, self.totalSymbols):
			singleSymbol = Symbol(x, y, self.speed)
			self.symbols.append(singleSymbol)
			x -= symbolSize

	def render(self):
		for eachSymbol in self.symbols:
			arrs[eachSymbol.row][eachSymbol.column] = " "
			eachSymbol.rain()
			arrs[eachSymbol.row][eachSymbol.column] = eachSymbol.value
			eachSymbol.setRandomSymbol()





if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("The matrix has stopped")