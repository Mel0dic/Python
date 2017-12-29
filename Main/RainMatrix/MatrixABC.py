import sys, time, random, os



#Detect the operating system and clears terminal with apropriate command
os.system('cls' if os.name == 'nt' else 'clear')

#Get's the terminal size
column, row = os.get_terminal_size()

#Create variable symbolSize set to 1
symbolSize = 1

#Create an array of Spaces the height and width of the terminal
arrs = [[" "] * column for i in range(row)]

#Initialise streams array
streams = []




def main():
	#Declare arrs, colimn and row as global vars
	global arrs, column, row

	#Set stringer to an empty string
	STRINGER = ""
	#Set x to 0
	x = 0
	#Loop from 0 to width of terminal
	for i in range(0, column):
		#Set stream to class stream
		stream = Stream()
		#Generate random number from top to bottom of terminal -5
		y = random.randint(0, row-5)
		#Geneate random symbol at point x, y
		stream.generateSymbols(y, x)
		#Append the streams array with class just made
		streams.append(stream)
		#add 1 to x
		x += 1

	#Create infinite loop
	while 1:
		#For i in height of terminal
		for i in range(row):
			#Join row to stringer
			STRINGER += "".join(arrs[i])
		#For stream in streams
		for stream in streams:
			#Render each stream
			stream.render()
		#Detect the operating system and clears terminal with apropriate command
		os.system('cls' if os.name == 'nt' else 'clear')
		#Print out Stringer
		print(STRINGER)
		#Set stringer to an empty string again
		STRINGER = ""
		#Sleep for 0.1 second
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
			self.value = chr(0 + random.randint(33, 126))
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
		self.speed = 1

	def generateSymbols(self, x, y):
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