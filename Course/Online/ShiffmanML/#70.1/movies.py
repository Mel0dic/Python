#From https://www.youtube.com/watch?v=N8Fabn1om2k&list=PLRqwX-V7Uu6bCN8LKrcMa6zF4FPtXyXYj&index=2

import json, math
from pprint import pprint

nameData = {}





def main():
	data = json.load(open('ratrings.json'))

	for something in data["users"]:
		nameData[something["name"]] = something
		nameData[something["name"]].pop("timestamp")
		nameData[something["name"]].pop("name")

	#euclideanDistance("Alca", "Unicorn")
	pprint(findNearestNeighbours("Alca"))






def euclideanDistance(name1, name2):

	person1 = list(nameData[name1].values())
	person2 = list(nameData[name2].values())

	squaresSum = 0

	for i in range(0, len(person1)):
		try:
			difference = person1[i] - person2[i]
		except TypeError:
			difference = 0

		squaresSum += difference * difference

	sqRoot = math.sqrt(squaresSum)

	similarity = 1/(1 + sqRoot)

	return(similarity)





def findNearestNeighbours(name):
	
	similarityScores = {}

	for i in nameData:
		other = i
		if name != other:
			similarity = euclideanDistance(name, other)
			similarityScores[other] = similarity
		else:
			similarityScores[other] = -1

	return similarityScores





def compareSimilarity(a, b):
	score1 = similarityScores[a.name]
	score2 = similarityScores[b.name]

	return score2 - score1






if __name__ == "__main__":
	main()