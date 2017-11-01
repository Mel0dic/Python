import random

bank = ["al", "en", "da", "fu", "el", "kar", "tuk", "la", "bel", "fol", "be", "wol"]
classes = ["B", "E", "W", "D", "K"]

def main():
	for i in range(10):
		newClass = CharClass
		newClass.nameGenerator()
		classArr.append[newClass]
	return 1

class CharClass:
	def __init__(self):
		self.name = ""
		self.type, self.health, self.power, self.SAP, self.speed = self.typeGenerator()

	def nameGenerator(self):
		tempName = ""
		for i in range(random.randrange(3, 5)):
			tempName += bank[random.randrange(0, len(bank))]
		self.Name = tempName
	
	def typeGenerator(self):
		tempClass = classes[random.randrange(0, len(classes))]
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

main()