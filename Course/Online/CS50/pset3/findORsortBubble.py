'''
Search and a sort algorithm
'''

def main():
	arrayOfNumbs = [12, 10, 5, 14, 3, 12, 9, 8, 7, 5, 13]
	sortednumbs = sort(arrayOfNumbs, len(arrayOfNumbs))
	print(search(3, sortednumbs, len(arrayOfNumbs)))


#Binary Search
#Search algorithm requires value to be sorted in size order
#Define search with target value list of numbers and size of array
def search(target, values, n):
	#If length of array less than 0 return False
	if n < 0:
		return False
	#Set minNum to 0
	minNum = 0
	#Set maxNum to n-1
	maxNum = n-1

	#While n is greater than 0
	while n > 0:
		half = int((minNum + maxNum) / 2)
		if values[half] == target:
			return True
		elif values[half] < target:
			minNum = half + 1
		else:
			maxNum = half-1
		n = maxNum - minNum + 1
	return False


#Bubble Sort
#Define a number sorting algorithm with array of values and n length of array or use .sort
#you know who cares
def sort(values, n):
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
	return values

if __name__ == "__main__":
	main()