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
	return listToSort