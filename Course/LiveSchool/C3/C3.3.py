import random

bank = ["al", "en", "da", "fu", "el", "kar", "tuk", "la", "bel", "fol", "be", "wol"]
classes = ["B", "E", "W", "D", "K"]
classArr = []

def main():
	temporary = input("Would you like to load or generate a new team? (L or G) ")

	if temporary.upper() == "L":
		with open("classSave.txt", "r") as readFile:
			charachter = readFile.readlines()
		for i in charachter:
			newClass = CharClass(i)
	elif temporary.upper() == "G":
		for i in range(10):
			newClass = CharClass()
			newClass.nameGenerator()
			classArr.append(newClass)

		for i in classArr:
			i.printStats()


	tempYN = input("Would you like to edit or delete a charachter? (Y or N) ")

	if tempYN.upper() == "Y":
		while 1:
			removeORadd = input("Would you like to remove or add a charachter? (del or add) ")

			if removeORadd.lower() == "add":
				newClass = CharClass()
				newClass.nameGenerator()
				classArr.append(newClass)
			elif removeORadd.lower() == "del":
				nameEditorDel = input("input the name of the charachter you would like to delete: ")
				for i in range(len(classArr)):
					if classArr[i].name == nameEditorDel:
						edit = i
						break
				classArr.pop(i)

			tempYN = input("Would you like to print out your team? (Y or N) ")
			if tempYN.upper() == "Y":
				for i in classArr:
					i.printStats()
			
			finished = input("Are you finished editing your team? (Y or N) ")

			if finished.upper() == "Y":
				break

	tempYN = input("Would you like to save your team? (Y or N) ")

	if tempYN.upper() == "Y":
		classFileWrite = open("classSave.txt", "w")
		for i in classArr:
			classFileWrite.write(i.returnStats())
		classFileWrite.close()

	return 1

class CharClass:
	def __init__(self, types = None):
		if types == None:
			self.name = self.nameGenerator()
			self.type, self.health, self.power, self.SAP, self.speed = self.typeGenerator()
		else:
			types = types.split(", ")
			types[-1] = types[-1].strip()
			print(types)
			self.name, self.type, self.health, self.power, self.SAP, self.speed = types[0], types[1], types[2], types[3], types[4], types[5]


	def nameGenerator(self):
		tempName = ""
		for i in range(random.randrange(3, 5)):
			tempName += bank[random.randrange(0, len(bank))]
		self.name = tempName
	
	def typeGenerator(self, tempClass = classes[random.randrange(0, len(classes))]):
		if tempClass == "B":
			return "Barbarian", 100, 70, 20, 50
		elif tempClass == "E":
			return "Elf", 100, 30, 60, 10
		elif tempClass == "W":
			return "Wizard", 100, 50, 70, 30
		elif tempClass == "D":
			return "Dragon", 100, 90, 40, 50
		elif tempClass == "K":
			return "Knight", 100, 60, 10, 60

	def printStats(self):
		print("Name: %12s, Type: %9s, Health: %i, Power: %i, SAP: %i, Speed: %i" %(self.name, self.type, self.health, self.power, self.SAP, self.speed))

	def returnStats(self):
		return ("%s, %s, %i, %i, %i, %i\n" %(self.name, self.type, self.health, self.power, self.SAP, self.speed))

main()