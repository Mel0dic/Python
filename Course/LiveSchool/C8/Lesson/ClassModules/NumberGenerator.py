from random import randint

def arrayGenerator(lengthOfarray):
	randomNumberArray = []
	for i in range(lengthOfarray):
		randomNumberArray.append(randint(0, lengthOfarray))
	return randomNumberArray