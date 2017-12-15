def bubbleSort(listToSort):
	#Set isSwapMade to true to create a makeshift do while loop
	isSwapMade = True
	#while a swap has been made in the iteraton of the list
	while isSwapMade:
		#Set isSwapMade to false
		isSwapMade = False
		#For i in range 0 to length of array
		for i in range(0, len(listToSort)-1):
			#If value at listToSort[i] < value at listToSort[i-1]
			if listToSort[i] > listToSort[i+1]:
				#Swap the values
				listToSort[i], listToSort[i+1] = listToSort[i+1], listToSort[i]
				#set isSwapMade = True
				isSwapMade = True
	return listToSort