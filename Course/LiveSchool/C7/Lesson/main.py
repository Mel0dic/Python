def bubbleSort(values, n):
	#initialize a count for amount of iterations
	count = 0
	#Set is sorted to false
	isSorted = False
	#For i in range 0 to length of array + 1
	while not isSorted:
		#Set isSorted to true
		isSorted = True
		#For j in range 0 to length of array
		for j in range(1, n):
			#If value at values[j] < value at values[j-1]
			if values[j] < values[j-1]:
				#Set Holder == value at values[j]
				holder = values[j]
				#Set values[j] to value at values[j-1]
				values[j] = values[j-1]
				#Set value at values[j] to value at values[j-1]
				values[j-1] = holder
				#set isSorted = False
				isSorted = False
		print(values)
		#Count iteration
		count += 1
	print(count)
	return values

testArray = [3, 5, 8, 17, 12, 15, 18, 23, 1]

print(bubbleSort(testArray, len(testArray)))