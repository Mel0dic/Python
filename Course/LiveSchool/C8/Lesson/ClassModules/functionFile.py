from random import randint

def arrayGenerator(lengthOfarray):
	randomNumberArray = []
	for i in range(lengthOfarray):
		randomNumberArray.append(randint(0, lengthOfarray))
	return randomNumberArray

def bubbleSort(listToSort):
	#Set is sorted to false
	isSorted = False
	#For i in range 0 to length of array + 1
	while not isSorted:
		#Set isSorted to true
		isSorted = True
		#For j in range 0 to length of array
		for j in range(1, len(listToSort)):
			#If value at listToSort[j] < value at listToSort[j-1]
			if listToSort[j] < listToSort[j-1]:
				#Set Holder == value at listToSort[j]
				holder = listToSort[j]
				#Set listToSort[j] to value at listToSort[j-1]
				listToSort[j] = listToSort[j-1]
				#Set value at listToSort[j] to value at listToSort[j-1]
				listToSort[j-1] = holder
				#set isSorted = False
				isSorted = False
	return listToSort

def insertionSort(listToSort):
	#Loop through numbers 1 to length of list
	for i in range(1, len(listToSort)):
		#Set the end of the sorted list to 1 below current number in loop
		endSorted = i - 1
		#Set itemToSort to item currently being sorted
		itemToSort = listToSort[i]
		#While point in list at point endSorted is > item being sorted
		while (listToSort[endSorted] > itemToSort) and (endSorted >= 0):
			#set point at endSorted + 1 to data value at endSorted moving \
			# the values to the right
			listToSort[endSorted + 1] = listToSort[endSorted]
			#Take 1 away from endSorted
			endSorted -= 1
		#After point in list for value to sort is found put value at that point
		listToSort[endSorted + 1] = itemToSort