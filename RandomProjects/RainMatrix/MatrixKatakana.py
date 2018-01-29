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
		#Set row variable to x making sure its a whole number
		self.row = int(x)
		#Set row variable to y making sure its a whole number
		self.column= int(y)
		#Set speed variable to speed
		self.speed = speed
		#Set switch interval to 0 for a 100% chance of generating symbol
		self.switchInterval = 0
		#Set the value of symbol to none
		self.value = None

	#Define function to generate random symbol with a 1/4 chance or 1/1 if first time
	def setRandomSymbol(self):
		#If switch interval is < 25 generate a new random symbol
		if self.switchInterval <= 25:
			#Set value to char value of random number between 33 and 126
			self.value = chr(0x30A0 + random.randint(0, 96)) ##### Problem with char size pushing lines breaks shit fuck that
			#Set the char in the array to the generated value
			arrs[self.row][self.column] = self.value
		#Call symbolSwitch to generate new number between 1, 100 for a 1/4 chance of changing symbol-
		#when setRandomSymbol is next called
		self.symbolSwitch()

	#Def rain
	def rain(self):
		#Set row to 0 if symbol will be onscreen else move down speed
		self.row = 0 if self.row + self.speed >= row else self.row + self.speed			

	#Def symbolSwitch to generate random number between 1, 100 set to switchInterval
	def symbolSwitch(self):
		self.switchInterval = random.randint(1, 100)




class Stream:
	def __init__(self):
		#Initiate empty symbols array
		self.symbols = []
		#Set total symbols to a random number between 3 and 10
		self.totalSymbols = random.randint(3, 10)
		#Set speed to 1
		self.speed = 1

	#Define generateSymbols to generate random symbols for the trail above original letter
	def generateSymbols(self, x, y):
		#Loop from 0 to totalSymbols
		for i in range(0, self.totalSymbols):
			#Set singleSymbol to new generated Symbol class
			singleSymbol = Symbol(x, y, self.speed)
			#Append symbols with class in singleSymbol
			self.symbols.append(singleSymbol)
			#Take symbolSize (1) away from x. So next symbol will be 1 above current symbol
			x -= symbolSize

	#Define render to edit the array being printed with symbols
	def render(self):
		#Loop through every symbol in the symbols array
		for eachSymbol in self.symbols:
			#Set the position of eachSymbol to a space
			arrs[eachSymbol.row][eachSymbol.column] = " "
			#Call eachSymbols rain function to move it down
			eachSymbol.rain()
			#Set the position of eachsymbol to the symbol in eachSymbol
			arrs[eachSymbol.row][eachSymbol.column] = eachSymbol.value
			#Generate a new symbol for randomSymbol
			eachSymbol.setRandomSymbol()



#If program is being run as main program
if __name__ == "__main__":
	#Run main() function and if KeyboardInterrupt received clear terminal and print the matrix has stopped
	try:
		main()
	except KeyboardInterrupt:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("The matrix has stopped")