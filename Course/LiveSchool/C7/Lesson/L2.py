#25, 34, 7, 41, 19, 5, 98
#25, 7, 34, 19, 5, 41, 98
#7, 25, 19, 5, 34, 41, 98
#7, 19, 5, 25, 34, 41, 98
#7, 5, 19, 25, 34, 41, 98
#5, 7, 19, 25, 34, 41, 98
#5, 7, 19, 25, 34, 41, 98


List = [3, 5, 8, 17, 12, 15, 18, 23, 1]
#SortedList = 0
#FOR element in range(sortedList+1, len(list)-1):
#	key = list[element]
#	j = i - 1
#	while j >= 0 and a[j]:
#		If elemnt > i and


def myInsertion(listToSort):
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
		print(listToSort)

myInsertion(List)

print(List)
